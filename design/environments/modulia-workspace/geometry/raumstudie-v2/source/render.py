import json,math
from pathlib import Path
import numpy as np
from PIL import Image
O=Path('outputs/modulia-raumstudie-v2')
mesh=json.loads((O/'mesh.json').read_text());model=json.loads((O/'raum-modell.json').read_text())
W,H=1200,800
def unit(v):return v/np.linalg.norm(v)
def clipped(v):
 out=[]
 for a,b in zip(v,v[1:]+v[:1]):
  ia=a[2]>.07;ib=b[2]>.07
  if ia:out.append(a)
  if ia!=ib:out.append(a+(.07-a[2])/(b[2]-a[2])*(b-a))
 return out
for key,cam in model['cameras'].items():
 eye=np.array(cam['eye']);f=unit(np.array(cam['target'])-eye);right=unit(np.cross([0,0,1],f));up=np.cross(f,right);basis=np.stack([right,up,f]);scale=600/math.tan(math.radians(cam['fov']/2))
 depth=np.full((H,W),np.inf);im=np.full((H,W,3),[244,237,223],dtype=np.uint8);edges=[]
 for obj in mesh:
  world=np.array(obj['v'],float);v=clipped([basis@(p-eye) for p in world])
  if len(v)<3:continue
  v=np.array(v);p=np.column_stack((600+scale*v[:,0]/v[:,2],400-scale*v[:,1]/v[:,2],1/v[:,2]))
  normal=np.cross(world[1]-world[0],world[2]-world[0]);normal=unit(normal)
  shade=.78+.22*abs(np.dot(normal,unit(np.array([.4,-.4,1.]))))
  c=obj['c'];color=np.array([int(c[i:i+2],16) for i in [1,3,5]])*shade
  for k in range(1,len(p)-1):
   a,b,c=p[0],p[k],p[k+1]
   x0=max(0,int(math.floor(min(a[0],b[0],c[0]))));x1=min(W-1,int(math.ceil(max(a[0],b[0],c[0]))))
   y0=max(0,int(math.floor(min(a[1],b[1],c[1]))));y1=min(H-1,int(math.ceil(max(a[1],b[1],c[1]))))
   if x1<x0 or y1<y0:continue
   det=(b[1]-c[1])*(a[0]-c[0])+(c[0]-b[0])*(a[1]-c[1])
   if abs(det)<1e-8:continue
   yy,xx=np.mgrid[y0:y1+1,x0:x1+1];xx=xx+.5;yy=yy+.5
   w0=((b[1]-c[1])*(xx-c[0])+(c[0]-b[0])*(yy-c[1]))/det
   w1=((c[1]-a[1])*(xx-c[0])+(a[0]-c[0])*(yy-c[1]))/det;w2=1-w0-w1
   iz=w0*a[2]+w1*b[2]+w2*c[2]
   z=1/np.maximum(iz,1e-12);d=depth[y0:y1+1,x0:x1+1]
   mask=(w0>=-1e-7)&(w1>=-1e-7)&(w2>=-1e-7)&(z<d)
   d[mask]=z[mask];im[y0:y1+1,x0:x1+1][mask]=color
  if not obj['tag'].startswith('Konsole'):edges.extend((a,b) for a,b in zip(p,np.roll(p,-1,axis=0)))
 for a,b in edges:
  # Clip screen lines before sampling so near-plane geometry remains bounded.
  delta=b-a;t0=0.;t1=1.
  for axis,lo,hi in [(0,0,W-1),(1,0,H-1)]:
   if abs(delta[axis])<1e-8:
    if not lo<=a[axis]<=hi:t1=-1
   else:
    q0=(lo-a[axis])/delta[axis];q1=(hi-a[axis])/delta[axis]
    t0=max(t0,min(q0,q1));t1=min(t1,max(q0,q1))
  if t1<t0:continue
  aa=a+t0*delta;bb=a+t1*delta;n=int(max(abs(bb[0]-aa[0]),abs(bb[1]-aa[1])))+1
  q=aa+np.linspace(0,1,n)[:,None]*(bb-aa);x=np.clip(q[:,0].astype(int),0,W-1);y=np.clip(q[:,1].astype(int),0,H-1);z=1/np.maximum(q[:,2],1e-12)
  ok=z<depth[y,x]+.012;im[y[ok],x[ok]]=[61,79,82]
 Image.fromarray(im).save(O/f'sicht-{key.lower()}.png')
 print(key,'rendered')

import re
h=O/'raumstudie.html'
s=h.read_text()
for key in model['cameras']:
 s=re.sub(r'(<section id="view-'+key+r'"[^>]*>).*?(</section>)',r'\1<img src="sicht-'+key.lower()+'.png" style="width:100%;height:auto" alt="Sicht '+key+' aus dem gemeinsamen Raummodell">'+r'\2',s,flags=re.S)
 (O/f'sicht-{key.lower()}.svg').unlink(missing_ok=True)
h.write_text(s)
