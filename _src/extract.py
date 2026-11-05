import re,html,sys
s=open(sys.argv[1],encoding='utf-8',errors='ignore').read()
body=s.split('<body',1)[1]
body=re.sub(r'<(script|style|noscript)[^>]*>.*?</\1>','',body,flags=re.S)
body=re.sub(r'<(h[1-6]|p|li|a|div|section|button|span)[^>]*>',lambda m:'\n' if m.group(1) in('h1','h2','h3','h4','h5','h6','p','li','div','section','button') else ' ',body)
t=html.unescape(re.sub(r'<[^>]+>','',body))
t=re.sub(r'[ \t﻿\xa0]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
sys.stdout.reconfigure(encoding='utf-8')
print(t[:int(sys.argv[2]) if len(sys.argv)>2 else 9000])
