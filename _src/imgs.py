import re,sys,glob
sys.stdout.reconfigure(encoding='utf-8')
for f in sys.argv[1:]:
    s=open(f,encoding='utf-8',errors='ignore').read()
    print("=====",f)
    urls=set(re.findall(r'https?://[^"\'\s()]+?\.(?:png|jpe?g|svg|webp|gif)',s))
    for u in sorted(urls): print(u)
    print("-- counters:",re.findall(r'data-value="([0-9.]+)"',s), re.findall(r'(?:data-suffix|data-prefix|data-append)="([^"]*)"',s))
    print("-- icons:",sorted(set(re.findall(r'fa-[a-z0-9-]{3,}',s)))[:40])
    print("-- bg:",re.findall(r'background-image:\s*url\(([^)]+)\)',s)[:10])
    print("-- iframes/videos:",re.findall(r'<(?:iframe|video|source)[^>]+(?:src|data-src)="([^"]+)"',s)[:10])
    print("-- pdf/other:",sorted(set(re.findall(r'https?://[^"\'\s()]+?\.(?:pdf|mp4)',s))))
