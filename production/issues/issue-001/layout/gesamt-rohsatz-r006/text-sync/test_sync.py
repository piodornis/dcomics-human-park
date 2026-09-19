import csv,importlib.util,json,shutil,subprocess,sys,tempfile
from pathlib import Path
script=Path(__file__).with_name('sync_texts.py')
spec=importlib.util.spec_from_file_location('sync',script);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
cases=[('unchanged','A','A','A',0,'A','A'),('native_edit','A','A','B',0,'B','B'),('csv_edit','A','B','A',0,'B','A'),('same_edit','A','B','B',0,'B','B'),('conflict','A','B','C',1,'B','A'),('unicode_multiline','A','A','„Grüße“,\nneue Zeile',0,'„Grüße“,\nneue Zeile','„Grüße“,\nneue Zeile')]
for name,base,csvtext,native,fail,expected,expectedbase in cases:
 with tempfile.TemporaryDirectory() as folder:
  root=Path(folder);work=root/'text-sync';work.mkdir();shutil.copy2(script,work/script.name)
  m.write(root/'lettering.csv',m.csv_data([{'text_id':'T1','text':csvtext}],['text_id','text']))
  m.write(work/'native-texts.csv',m.csv_data([{'text_id':'T1','text':native}],['text_id','text']))
  (work/'baseline.json').write_text(json.dumps({'texts':{'T1':base}}));(work/'export-status.txt').write_text('test fixture')
  m.write(root/'text-changes.csv',m.csv_data([],['timestamp','text_id','old_text','new_text','direction','export_sha256']))
  result=subprocess.run([sys.executable,str(work/script.name),'--apply'],capture_output=True,text=True)
  assert bool(result.returncode)==bool(fail),(name,result.stderr,result.stdout)
  assert m.read_rows(root/'lettering.csv')[0]['text']==expected,name
  assert json.loads((work/'baseline.json').read_text())['texts']['T1']==expectedbase,name
print('PASS: unchanged, native-only, CSV-only, matching edits, conflicts, Unicode/multiline round trip.')
