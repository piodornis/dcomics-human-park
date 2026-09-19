"""Read-only InDesign export -> editable lettering CSV, with three-way conflict detection."""
import argparse,csv,hashlib,io,json,os,re,shutil,time
from datetime import datetime,timezone
from pathlib import Path

def read_rows(path):
    with path.open(encoding='utf-8-sig',newline='') as f:
        rows=list(csv.DictReader(f))
    ids=[r['text_id'] for r in rows]
    if any(not x for x in ids) or len(ids)!=len(set(ids)):
        raise ValueError('Missing or duplicate text IDs: '+str(path))
    return rows

def decide(base,csv_value,native):
    if csv_value==native:
        return 'equal',csv_value,csv_value
    if csv_value==base:
        return 'native_to_csv',native,native
    if native==base:
        return 'csv_pending',csv_value,base
    return 'conflict',csv_value,base

def csv_data(rows,fields):
    s=io.StringIO(newline='');w=csv.DictWriter(s,fieldnames=fields,lineterminator='\n');w.writeheader();w.writerows(rows);return s.getvalue()

def write(path,content):
    temp=path.with_suffix(path.suffix+'.tmp')
    with temp.open('w',encoding='utf-8',newline='') as f:f.write(content)
    os.replace(temp,path)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--init',action='store_true');ap.add_argument('--apply',action='store_true');args=ap.parse_args()
    here=Path(__file__).resolve().parent;project=here.parent
    native_path=here/'native-texts.csv';base_path=here/'baseline.json';target=project/'lettering.csv'
    if time.time()-native_path.stat().st_mtime>600:
        raise SystemExit('Export is older than 10 minutes. Run export-indesign.jsx again before syncing.')
    native=read_rows(native_path);nm={r['text_id']:r for r in native}
    stamp=datetime.now(timezone.utc).isoformat();digest=hashlib.sha256(native_path.read_bytes()).hexdigest()
    meta={'export_sha256':digest,'export_status':(here/'export-status.txt').read_text(),'captured_at':stamp}
    fields=['text_id','physical_position','slot','story_page','panel_id','kind','text','source_ref','native_story_id']
    if args.init:
        if target.exists() or base_path.exists():raise SystemExit('Baseline already exists. Refusing to overwrite.')
        layout=json.loads((project/'layout.json').read_text());panels={q['panel_id']:q for q in layout['panels']};rows=[];differences=[]
        for r in sorted(native,key=lambda r:(int(r['physical_position']),r['text_id'])):
            tid=r['text_id'];match=re.match(r'(S\d{3}-P\d{2})-',tid);pid=match[1] if match else '';q=panels.get(pid,{})
            story=bool(pid and tid.endswith('-TEXT'))
            kind=('document' if pid=='S016-P01' else 'caption') if story else ('placeholder' if any(x in tid for x in ['PLACEHOLDER','OPEN','MISSING','STATUS','OPTION']) else 'editorial')
            rows.append({'text_id':tid,'physical_position':r['physical_position'],'slot':r['page_label'].split(' / ')[0],'story_page':q.get('story_page',''),'panel_id':pid,'kind':kind,'text':r['text'],'source_ref':q.get('source','Native layout r005; editorial/placeholder working text'),'native_story_id':r['native_story_id']})
            if story and r['text']!=q['text']:differences.append({'text_id':tid,'source_text':q['text'],'native_text':r['text']})
        write(target,csv_data(rows,fields));write(base_path,json.dumps({'metadata':meta,'texts':{r['text_id']:r['text'] for r in rows}},ensure_ascii=False,indent=2))
        write(here/'initial-comparison.json',json.dumps({'source_differences':differences,'metadata':meta},ensure_ascii=False,indent=2))
        write(project/'text-changes.csv',csv_data([],['timestamp','text_id','old_text','new_text','direction','export_sha256']))
        print(f'Initialized {len(rows)} text objects; {len(differences)} differences from Story layout. Native snapshot retained.');return
    baseline=json.loads(base_path.read_text());base=baseline['texts'];rows=read_rows(target);cm={r['text_id']:r for r in rows}
    if set(base)!=set(nm) or set(base)!=set(cm):
        issues={'native_added':sorted(set(nm)-set(base)),'native_missing':sorted(set(base)-set(nm)),'csv_added':sorted(set(cm)-set(base)),'csv_missing':sorted(set(base)-set(cm))}
        write(here/'sync-report.json',json.dumps({'state':'blocked_mapping','differences':issues},indent=2));raise SystemExit('Text objects added/removed/renamed. Explicit ID reconciliation required; CSV unchanged.')
    results=[];conflicts=[];nextbase=dict(base);events=[]
    for row in rows:
        tid=row['text_id'];action,value,common=decide(base[tid],row['text'],nm[tid]['text']);results.append({'text_id':tid,'action':action})
        if action=='conflict':conflicts.append({'text_id':tid,'base':base[tid],'csv':row['text'],'native':nm[tid]['text']})
        if action=='native_to_csv':events.append({'timestamp':stamp,'text_id':tid,'old_text':row['text'],'new_text':value,'direction':'InDesign -> CSV','export_sha256':digest})
        row['text']=value;nextbase[tid]=common
    report={'mode':'apply' if args.apply else 'dry_run','metadata':meta,'results':results,'conflicts':conflicts,'native_updates':len(events),'csv_only_pending':sum(r['action']=='csv_pending' for r in results)}
    write(here/'sync-report.json',json.dumps(report,ensure_ascii=False,indent=2))
    if conflicts:raise SystemExit('Conflicting edits detected. No CSV or baseline updated; see sync-report.json.')
    if args.apply:
        backup=here/'history'/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ');backup.mkdir(parents=True)
        for f in [target,base_path,project/'text-changes.csv']:shutil.copy2(f,backup/f.name)
        with (project/'text-changes.csv').open(encoding='utf-8',newline='') as f:history=list(csv.DictReader(f))
        write(target,csv_data(rows,list(rows[0])))
        write(project/'text-changes.csv',csv_data(history+events,['timestamp','text_id','old_text','new_text','direction','export_sha256']))
        write(base_path,json.dumps({'metadata':meta,'texts':nextbase},ensure_ascii=False,indent=2))
    print(f'{report["mode"]}: {len(events)} native updates; {report["csv_only_pending"]} CSV-only changes retained; no conflicts.')

if __name__=='__main__':main()
