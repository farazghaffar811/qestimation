import re,sys,glob,os,urllib.request,concurrent.futures
sys.stdout.reconfigure(encoding='utf-8')
urls=set()
for f in glob.glob('*.html'):
    s=open(f,encoding='utf-8',errors='ignore').read()
    urls|=set(re.findall(r'https?://[^"\'\s()]+?\.(?:png|jpe?g|webp|gif|pdf)',s))
urls={u for u in urls if not re.search(r'-\d+x\d+\.(jpe?g|png|webp)$',u) and 'gravatar' not in u and 'emoji' not in u}
def dl(u):
    name=u.rsplit('/',1)[1]
    if u.endswith('.pdf'): out='../assets/samples/'+name
    elif '/2022/06/' in u: out='../assets/gallery/'+name
    else: out='../assets/img/'+name
    if os.path.exists(out): return (u,'exists')
    try:
        req=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0 Chrome/124'})
        d=urllib.request.urlopen(req,timeout=40).read()
        if len(d)<200: return (u,'tiny')
        open(out,'wb').write(d); return (u,len(d))
    except Exception as e: return (u,'ERR '+str(e)[:60])
with concurrent.futures.ThreadPoolExecutor(8) as ex:
    for u,r in ex.map(dl,sorted(urls)):
        if r!='exists' and (isinstance(r,str)): print(r,u)
print("done",len(urls))
