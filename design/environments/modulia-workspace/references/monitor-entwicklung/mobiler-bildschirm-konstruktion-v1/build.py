from pathlib import Path
import json

out=Path('outputs/mobiler-bildschirm-konstruktion-v1')
parts=[]
def rect(x,y,w,h,fill,rx=6):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="#203b45" stroke-width="3"/>'
def circle(x,y,r,fill):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="#203b45" stroke-width="3"/>'
def text(x,y,s,size=18,anchor='middle'):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Arial,sans-serif" font-size="{size}" fill="#203b45">{s}</text>'

# Shared schematic units, not canonical dimensions. Display rotates about (0,210).
def chassis(rear):
    s=rect(-32,135,64,310,'#e8d8b8')
    s+=rect(-84,180,168,32,'#e8d8b8')
    for sign in [-1,1]:
        x=sign*84
        s+=rect(x-12,196,24,90,'#435b65')+circle(x,196,19,'#e6b84d')
        s+=circle(x,286,14,'#435b65')+rect(x-15,294,30,78,'#e8d8b8')
        s+=rect(x-13,375,26,28,'#435b65')
        s+=f'<path d="M{x-13},401 v16 h7 M{x+13},401 v16 h-7" fill="none" stroke="#203b45" stroke-width="6"/>'
        s+=rect(sign*38-12,437,24,60,'#435b65')
        s+=rect(sign*38-28,493,56,28,'#285d6b')
        s+=rect(sign*38-22,498,44,9,'#d8ccb2' if rear else '#e6b84d',2)
    s+=rect(-18,240,36,151,'#435b65')
    return s
def display(landscape,rear):
    w,h=(320,180) if landscape else (180,320)
    s=rect(-w/2,210-h/2,w,h,'#285d6b',10)
    if not rear:
        s+=rect(-w/2+10,210-h/2+10,w-20,h-20,'#66bdd0',5)
        s+=f'<path d="M{-w/2+25},210 H{w/2-25}" stroke="#dbf4ed" stroke-width="3"/>'
    else:
        s+=circle(0,210,46,'#d5a842')+circle(0,210,30,'#e8d8b8')
    return s

parts.append('<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="920" viewBox="0 0 1600 920">')
parts.append('<rect width="1600" height="920" fill="#f8f2e6"/>')
parts.append(text(60,55,'MOBILER BILDSCHIRM · KONSTRUKTION V1',30,'start'))
parts.append(text(60,87,'EXPLORATION / PROPOSAL · gleiche Skala · orthografisch · nur das Display dreht sich',18,'start'))
for i,(land,rear,label) in enumerate([(False,False,'VORNE · PORTRAIT'),(True,False,'VORNE · LANDSCAPE'),(False,True,'HINTEN · PORTRAIT'),(True,True,'HINTEN · LANDSCAPE')]):
    x=210+i*395
    parts.append(text(x,133,label,19))
    parts.append(f'<g transform="translate({x},110)">')
    parts.append('<path d="M0,110 V540 M-180,196 H180 M-180,521 H180" fill="none" stroke="#c3bbaa" stroke-dasharray="5 5"/>')
    parts.append((display(land,rear)+chassis(rear)) if rear else (chassis(rear)+display(land,rear)))
    parts.append('</g>')
    parts.append(text(x,669,'Fersen sichtbar' if rear else 'Fußspitzen nach vorne',16))
parts.append(text(60,725,'FEST: Korpus 64 · Schulterachsen ±84 · Schulterhöhe 196 · Displayzentrum (0, 210)',20,'start'))
parts.append(text(60,757,'DISPLAY: 180 × 320 → 320 × 180. Arme unverändert; im Querformat vorne teilweise verdeckt.',20,'start'))
parts.append(text(60,803,'Schichtfolge von vorne: Display → Drehlager → stationärer Korpus mit Schulterträger → Arme.',19,'start'))
parts.append(text(60,835,'Schematische Einheiten, keine Realmaße. Tiefe, Drehfreiraum und Faltung sind noch zu konstruieren.',18,'start'))
parts.append(text(60,873,'Die Rückansichten zeigen denselben schmalen Korpus. Keine ausfahrbaren oder mitdrehenden Schultern.',18,'start'))
parts.append('</svg>')
(out/'konstruktionsblatt.svg').write_text(''.join(parts))
(out/'konstruktion.json').write_text(json.dumps({'status':'EXPLORATION / PROPOSAL','units':'schematic','body_width':64,'shoulder_centers':[[-84,196],[84,196]],'display_center':[0,210],'portrait':[180,320],'landscape':[320,180],'arm_pose':'identical in all views','feet':'forward toward display front'},indent=2))
assert sorted([180,320])==sorted([320,180])
print('Vier Ansichten verwenden identische Korpus- und Armgeometrie.')
