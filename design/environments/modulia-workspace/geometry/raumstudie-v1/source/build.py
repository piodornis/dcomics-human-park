import math, json, html
from pathlib import Path
O=Path('outputs/modulia-raumstudie-v1'); O.mkdir(exist_ok=True)
W,L,H=4.8,5.6,3.0
model={'status':'PROPOSAL / EXPLORATION','units':'m','room':{'east_west':W,'north_south':L,'height':H},'axes':'x nach Ost/Fenster, y nach Süd, z nach oben; lokale Planrichtungen','door':{'wall':'West','y':[.65,1.75],'height':2.3},'window':{'wall':'Ost','y':[1.05,4.55],'z':[1.0,2.55]},'console':{'y':[2.0,4.8],'back_x':.90,'front_x':1.84,'back_bow':.10,'front_inset':.22,'height':.88},'cameras':{}}
faces=[]; objects=[]
def face(v,c,tag=''):
 faces.append({'v':v,'c':c,'tag':tag})
def box(name,x,y,z,dx,dy,dz,c):
 objects.append({'name':name,'origin':[x,y,z],'size':[dx,dy,dz]})
 p=[[x,y,z],[x+dx,y,z],[x+dx,y+dy,z],[x,y+dy,z],[x,y,z+dz],[x+dx,y,z+dz],[x+dx,y+dy,z+dz],[x,y+dy,z+dz]]
 for ids in [(0,3,2,1),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7),(4,5,6,7)]:face([p[i] for i in ids],c,name)
def wall_y(y,x0,x1,z0,z1,c):
 for i in range(math.ceil((x1-x0)/.6)):
  a=x0+i*.6;b=min(a+.6,x1);face([[a,y,z0],[b,y,z0],[b,y,z1],[a,y,z1]],c,'Wand')
def wall_x(x,y0,y1,z0,z1,c):
 for i in range(math.ceil((y1-y0)/.6)):
  a=y0+i*.6;b=min(a+.6,y1);face([[x,a,z0],[x,b,z0],[x,b,z1],[x,a,z1]],c,'Wand')
for i in range(8):
 for j in range(10):
  a=i*.6;b=j*.56;face([[a,b,0],[a+.6,b,0],[a+.6,b+.56,0],[a,b+.56,0]],'#e7d8bd','Boden')
wall_y(0,0,W,0,H,'#ded1b8');wall_y(L,0,W,0,H,'#e7ddca')
wall_x(0,0,.65,0,H,'#e9dcc6');wall_x(0,1.75,L,0,H,'#e9dcc6');wall_x(0,.65,1.75,2.3,H,'#e9dcc6')
wall_x(W,0,L,0,1.0,'#e9dcc6');wall_x(W,0,L,2.55,H,'#e9dcc6');wall_x(W,0,1.05,1,2.55,'#e9dcc6');wall_x(W,4.55,L,1,2.55,'#e9dcc6')
face([[W+.01,1.05,1],[W+.01,4.55,1],[W+.01,4.55,2.55],[W+.01,1.05,2.55]],'#a7cbd1','Fenster')
for y in [1.05,4.50]:box('Fensterrahmen',W-.06,y,.96,.08,.05,1.64,'#526e70')
for z in [.96,2.55]:box('Fensterrahmen',W-.06,1.05,z,.08,3.5,.05,'#526e70')
box('Fensterbank',W-.24,1.02,.96,.27,3.56,.05,'#faf0db')
# West wall has real thickness around the opening, not an arbitrary overlay.
box('Türlaibung Nord',-.22,.60,0,.23,.05,2.35,'#526e70');box('Türlaibung Süd',-.22,1.75,0,.23,.05,2.35,'#526e70');box('Türsturz',-.22,.60,2.3,.23,1.2,.05,'#526e70')
# An open junction outside: left when leaving means south (+y).
for j in range(6):face([[-1.5,.55+j*.55,0],[0,.55+j*.55,0],[0,1.10+j*.55,0],[-1.5,1.10+j*.55,0]],'#d4c3a6','Vorraum')
wall_x(-1.5,.55,.65,0,2.5,'#dbc6a8');wall_x(-1.5,1.75,3.85,0,2.5,'#dbc6a8')
box('Außentür Nord',-1.55,.60,0,.1,.07,2.3,'#6d7b72');box('Außentür Süd',-1.55,1.73,0,.1,.07,2.3,'#6d7b72');box('Außentür Sturz',-1.55,.60,2.3,.1,1.20,.06,'#6d7b72')
box('Felsen seitlich im Vorraum',-1.30,.14,0,.62,.39,1.8,'#bf8662')
# Archive and fixed small cabinets: no mobile pedestal.
box('Archiv Unterbau',.22,.02,0,4.20,.50,.86,'#37616b');box('Archiv Arbeitsplatte',.20,.01,.86,4.24,.53,.055,'#f4ead6')
box('Archiv Rücken',.24,.015,.92,4.16,.15,1.25,'#315361')
for z in [.94,1.26,1.58,1.90]:
 box('Archiv Fachboden',.24,.03,z,4.16,.40,.035,'#466672')
 for k in range(10):
  # preserve one explicit upper plant bay near entrance
  if k==0 and z>=1.58:continue
  box('Archiv Modul',.28+k*.406,.09,z+.04,.36,.32,.235,'#bec3b8')
box('Archiv Oberschrank',.24,.03,2.22,3.65,.41,.49,'#37616b')
box('K1 fester Eckschrank',4.30,.58,0,.48,.58,.86,'#547276');box('K1 Platte',4.28,.56,.86,.52,.62,.055,'#f4ead6')
box('K1 Gerät',4.37,.65,.92,.31,.32,.35,'#aeb5af')
box('K2 fester Fensterschrank',4.28,4.65,0,.50,.74,.77,'#37616b');box('K2 Platte',4.26,4.63,.77,.54,.78,.05,'#f4ead6')
box('K2 Gerätebox',4.30,4.72,.82,.29,.28,.18,'#315d6f')
# A single console mesh, shared by every projection.
def curve(t):
 y=2+2.8*t;s=math.sin(math.pi*t);return (.90-.10*s,1.84-.22*s,y)
for i in range(24):
 a,b,y=curve(i/24);c,d,v=curve((i+1)/24)
 face([[a,y,.82],[c,v,.82],[d,v,.82],[b,y,.82]],'#f7edd7','Konsole Platte')
 face([[a,y,.88],[b,y,.88],[d,v,.88],[c,v,.88]],'#f7edd7','Konsole Platte')
 for x1,x2 in [(a,c),(b,d)]:
  face([[x1,y,.05],[x2,v,.05],[x2,v,.82],[x1,y,.82]],'#386272','Konsole')
  face([[x1,y,.82],[x2,v,.82],[x2,v,.88],[x1,y,.88]],'#eee0c3','Konsole Rand')
for t in [0,1]:
 a,b,y=curve(t);face([[a,y,.05],[b,y,.05],[b,y,.88],[a,y,.88]],'#466e78','Konsole Ende')
# Working doors occupy three longitudinal intervals; handles on east side.
for t in [.11,.5,.89]:
 a,b,y=curve(t);box('Frontgriff',b+.006,y-.06,.64,.024,.12,.035,'#213b49')
monitors=[]
for n,cy in enumerate([2.37,3.06],1):
 box('Monitorfuß '+str(n),1.02,cy-.17,.88,.40,.34,.035,'#345568')
 box('Monitorständer '+str(n),1.16,cy-.04,.91,.055,.08,.24,'#365368')
 box('Monitorgehäuse '+str(n),1.18,cy-.32,1.09,.07,.64,.86,'#294653')
 face([[1.253,cy-.29,1.13],[1.253,cy+.29,1.13],[1.253,cy+.29,1.91],[1.253,cy-.29,1.91]],'#58adc3','Bildschirm Vorderseite')
 monitors.append({'center':[1.215,cy,1.52],'width':.64,'height':.86})
box('Gelbe Ablage',1.14,4.27,.88,.43,.35,.055,'#d9ab36')
for y in [4.30,4.47]:box('Prüfmodul',1.21,y,.94,.27,.11,.055,'#9ba7a9')
def plant(name,x,y,z,size=.28):
 box(name+' Topf',x-size/2,y-size/2,z,size,size,size*.85,'#eee5d1')
 for k in range(7):
  q=2*math.pi*k/7;cx=x+math.cos(q)*size;cy=y+math.sin(q)*size
  face([[x,y,z+size*.7],[cx,cy,z+size*2.5],[x+math.cos(q+.3)*size*.5,y+math.sin(q+.3)*size*.5,z+size*2.15]],'#63875b',name)
box('P2 erhöhte Pflanzenablage',.24,.04,1.58,.44,.52,.045,'#eee0c3')
plant('P1 Tischpflanze',1.21,4.68,.88,.24);plant('P2 Archivpflanze hoch',.45,.29,1.63,.26);plant('P3 Hängepflanze',4.15,.23,2.24,.22)
plant('P4 Fensterbank',4.64,2.35,1.01,.20);plant('P5 Fensterschrank',4.54,5.18,.82,.22)
model['objects']=objects;model['monitors']=monitors
cams={'A':{'eye':[3.25,5.40,1.62],'target':[2.35,.15,1.35],'fov':72},'B':{'eye':[3.05,.82,1.62],'target':[2.70,5.5,1.35],'fov':76},'C':{'eye':[4.68,2.8,1.62],'target':[.2,2.8,1.35],'fov':78},'D':{'eye':[-.12,1.15,1.62],'target':[4.8,2.83,1.42],'fov':74}}
model['cameras']=cams
def sub(a,b):return [x-y for x,y in zip(a,b)]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def norm(a):
 l=math.sqrt(dot(a,a));return [v/l for v in a]
def clip(v):
 out=[]
 for a,b in zip(v,v[1:]+v[:1]):
  ia=a[2]>.07;ib=b[2]>.07
  if ia:out.append(a)
  if ia!=ib:
   t=(.07-a[2])/(b[2]-a[2]);out.append([a[k]+t*(b[k]-a[k]) for k in range(3)])
 return out
def render(cam):
 e=cam['eye'];f=norm(sub(cam['target'],e));r=norm(cross([0,0,1],f));u=cross(f,r);scale=600/math.tan(math.radians(cam['fov']/2))
 polys=[]
 for obj in faces:
  v=[]
  for p in obj['v']:
   q=sub(p,e);v.append([dot(q,r),dot(q,u),dot(q,f)])
  v=clip(v)
  if len(v)<3:continue
  points=[(600+scale*p[0]/p[2],400-scale*p[1]/p[2]) for p in v]
  if all(x<0 for x,y in points) or all(x>1200 for x,y in points) or all(y<0 for x,y in points) or all(y>800 for x,y in points):continue
  pts=' '.join(f'{x:.2f},{y:.2f}' for x,y in points)
  polys.append((sum(p[2] for p in v)/len(v),f'<polygon points="{pts}" fill="{obj["c"]}" stroke="#38515a" stroke-width="0.6" stroke-linejoin="round"><title>{html.escape(obj["tag"])}</title></polygon>'))
 polys.sort(reverse=True,key=lambda x:x[0])
 return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800"><rect width="1200" height="800" fill="#f4eddf"/>'+''.join(v for z,v in polys)+'</svg>'
for name,c in cams.items():(O/f'sicht-{name.lower()}.svg').write_text(render(c))
(O/'raum-modell.json').write_text(json.dumps(model,indent=2,ensure_ascii=False))
# True top view from same coordinates, including the unbuilt corridor continuation.
scale=90;ox=210;oy=90
def xy(x,y):return ox+x*scale,oy+y*scale
def rect(x,y,dx,dy,col):
 a,b=xy(x,y);return f'<rect x="{a}" y="{b}" width="{dx*scale}" height="{dy*scale}" fill="{col}" stroke="#36535c"/>'
plan='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 760"><rect width="920" height="760" fill="#faf5eb"/><g font-family="Arial" fill="#284752">'
plan+=rect(0,0,W,L,'#ede1cb')+rect(-1.5,.6,1.5,3.3,'#e5d5bc')
for ob in objects:
 if ob['name'] in ['Archiv Unterbau','K1 fester Eckschrank','K2 fester Fensterschrank']:
  x,y,z=ob['origin'];dx,dy,dz=ob['size'];plan+=rect(x,y,dx,dy,'#79969a')
pts=[]
for i in range(25):a,b,y=curve(i/24);pts.append(xy(a,y))
for i in reversed(range(25)):a,b,y=curve(i/24);pts.append(xy(b,y))
plan+='<polygon points="'+' '.join(f'{x},{y}' for x,y in pts)+'" fill="#f8edd4" stroke="#294f5c" stroke-width="3"/>'
for cy in [2.37,3.06]:plan+=rect(1.18,cy-.32,.07,.64,'#2996ad')
for x,y,label in [(1.21,4.68,'P1'),(.45,.29,'P2'),(4.15,.23,'P3'),(4.64,2.35,'P4'),(4.54,5.18,'P5')]:
 a,b=xy(x,y);plan+=f'<circle cx="{a}" cy="{b}" r="11" fill="#608b57"/><text x="{a+14}" y="{b+4}" font-size="12">{label}</text>'
x,y=xy(W,1.05);plan+=f'<path d="M{x},{y} v{3.5*scale}" stroke="#55a6bd" stroke-width="8"/>'
x,y=xy(0,.65);plan+=f'<path d="M{x},{y} v{1.1*scale}" stroke="#faf5eb" stroke-width="8"/>'
for name,c in cams.items():
 x,y=xy(*c['eye'][:2]);tx,ty=c['target'][:2];ex,ey=c['eye'][:2];a=math.atan2(ty-ey,tx-ex)
 for q in [a-math.radians(c['fov']/2),a+math.radians(c['fov']/2)]:
  xx,yy=xy(ex+math.cos(q)*1.25,ey+math.sin(q)*1.25);plan+=f'<path d="M{x},{y} L{xx},{yy}" stroke="#c08b40" stroke-dasharray="5 4"/>'
 plan+=f'<circle cx="{x}" cy="{y}" r="14" fill="#284f61"/><text x="{x}" y="{y+5}" text-anchor="middle" fill="white" font-size="14">{name}</text>'
plan+='<text x="210" y="40" font-size="24">Modulia · gemeinsames Raumgerüst v1</text><text x="210" y="65" font-size="15">PROPOSAL · 4,80 × 5,60 m · Höhe 3,00 m</text><text x="340" y="118" font-size="14">Archiv / Nord</text><text x="655" y="325" font-size="15">Fenster / Ost</text><text x="40" y="425" font-size="14">Gang nach links</text><text x="40" y="446" font-size="13">beim Hinausgehen ↓</text><text x="65" y="135" font-size="13">Außentür ←</text><text x="700" y="170" font-size="14">K1: Eckschrank</text><text x="700" y="555" font-size="14">K2: Fensterschrank</text><text x="210" y="650" font-size="15">P1 Tisch · P2 hohe Ablage · P3 oben am Archiv</text><text x="210" y="675" font-size="15">P4 Fensterbank · P5 niedriger Fensterschrank</text><text x="210" y="715" font-size="14">Maße und Kameras sind Vorschläge, keine Bestandsvermessung.</text></g></svg>'
(O/'grundriss.svg').write_text(plan)
# Review panel is a standalone project deliverable, not a new illustrated design.
svgs={n:(O/(('grundriss' if n=='Plan' else 'sicht-'+n.lower())+'.svg')).read_text() for n in ['Plan','A','B','C','D']}
head='<!doctype html><html lang="de"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Modulia – Raumstudie v1</title><style>body{font:16px system-ui;background:#faf5eb;color:#294954;margin:24px auto;max-width:1100px;padding:0 16px}button{font:inherit;padding:10px 20px;border:1px solid #59747a;border-radius:5px;background:#fff8e9;color:#294954;cursor:pointer}button[aria-pressed=true]{background:#294954;color:white}nav{display:flex;gap:8px;flex-wrap:wrap}section svg{width:100%;max-height:72vh}small{line-height:1.6}h1{font-size:26px}p{max-width:850px}</style><h1>Modulia · Raumstudie v1</h1><p>PROPOSAL / EXPLORATION · Ein gemeinsames Modell für vier Ansichten. Farben kennzeichnen Bauteile; Pflanzen und Felsen sind Platzhalter. Keine neue Stilentscheidung.</p><nav>'
for n in svgs:head+=f'<button data-view="{n}" aria-pressed="{str(n=="Plan").lower()}">{"Grundriss" if n=="Plan" else "Sicht "+n}</button>'
head+='</nav>'
for n,s in svgs.items():head+=f'<section id="view-{n}" {"" if n=="Plan" else "hidden"}>{s}</section>'
head+='<p id="caption">Maßvorschlag: 4,80 × 5,60 × 3,00 m. Der Gang verläuft links beim Hinausgehen.</p><small>Gestalterische Referenz bleibt modulia-workspace-01. Aktuelle SELECTED-Bilder unverändert. Der Plan definiert Lage und Abstände; die einfache Perspektivdarstellung ersetzt noch keine gestalterische Freigabe.</small><script>const notes={Plan:"Maßvorschlag: 4,80 × 5,60 × 3,00 m. Der Gang verläuft links beim Hinausgehen.",A:"A · Blick von Süd zum Archiv. Vorderseiten der Monitore.",B:"B · Blick von der Archivseite nach Süd. Eingang liegt hinter der Kamera.",C:"C · Blick vom Fenster nach West. Eingang im rechten Bildteil.",D:"D · Kamera an der Türschwelle. Standort, Blickrichtung und Bildwinkel gemeinsam festgelegt."};document.querySelectorAll("button[data-view]").forEach(b=>b.onclick=()=>{document.querySelectorAll("section").forEach(s=>s.hidden=s.id!=="view-"+b.dataset.view);document.querySelectorAll("button[data-view]").forEach(x=>x.setAttribute("aria-pressed",x===b));document.getElementById("caption").textContent=notes[b.dataset.view];});</script></html>'
(O/'raumstudie.html').write_text(head)
(O/'mesh.json').write_text(json.dumps(faces))
print('Built model, plan and four camera views:',len(faces),'faces')
