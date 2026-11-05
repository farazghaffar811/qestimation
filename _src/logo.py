from PIL import Image, ImageFilter
import numpy as np
im=np.array(Image.open('assets/img/logo-source.webp').convert('RGB')).astype(float)
H,W,_=im.shape
L=im.mean(axis=2); chroma=im.max(axis=2)-im.min(axis=2)
a=np.clip(np.maximum((chroma-12)/30,(165-L)/50),0,1)
# kill isolated specks: median-ish via blur threshold
A=Image.fromarray((a*255).astype(np.uint8)).filter(ImageFilter.MedianFilter(3)); a=np.array(A).astype(float)/255
b=230.0
f=np.where(a[...,None]>0,(im-(1-a[...,None])*b)/np.maximum(a[...,None],1e-3),im); f=np.clip(f,0,255)
img=Image.fromarray(np.dstack([f,a*255]).astype(np.uint8),'RGBA')
mask=a>0.15
ysn,xsn=np.where(mask); box=(int(xsn.min()),int(ysn.min()),int(xsn.max()+1),int(ysn.max()+1)); print("bbox",box)
logo=img.crop(box); logo.save('assets/img/logo.png'); print("logo",logo.size)
colsum=mask.sum(axis=0); gap=[x for x in range(300,W) if colsum[x]==0]; gx=gap[0]; print("gap",gx)
m2=mask[:,:gx]; ys2,xs2=np.where(m2); eb=(int(xs2.min()),int(ys2.min()),int(xs2.max()+1),int(ys2.max()+1))
em=img.crop(eb); side=max(em.size)+8; sq=Image.new('RGBA',(side,side),(0,0,0,0)); sq.paste(em,((side-em.size[0])//2,(side-em.size[1])//2))
sq.save('assets/img/logo-mark.png')
for n,s in [('icon-512',512),('icon-192',192),('apple-touch-icon',180),('favicon',64)]: sq.resize((s,s),Image.LANCZOS).save(f'assets/img/{n}.png')
arr=np.array(logo).astype(float); rgb=arr[...,:3]; isnavy=(rgb[...,2]>rgb[...,0]+10)
w=arr.copy(); w[...,:3][isnavy]=[255,255,255]; Image.fromarray(w.astype(np.uint8),'RGBA').save('assets/img/logo-white.png')
og=Image.new('RGBA',(1200,630),(28,38,70,255)); wl=Image.open('assets/img/logo-white.png'); wl.thumbnail((880,380)); og.paste(wl,((1200-wl.size[0])//2,(630-wl.size[1])//2-30),wl); og.convert('RGB').save('assets/img/og-image.jpg',quality=88)
chk=Image.new('RGBA',logo.size,(40,200,90,255)); chk.alpha_composite(logo); chk.convert('RGB').save('_src/logo-check.jpg',quality=80)
chk=Image.new('RGBA',(1200,630),(40,200,90,255)); chk.alpha_composite(Image.open('assets/img/og-image.jpg').convert('RGBA')); 
print("done")
