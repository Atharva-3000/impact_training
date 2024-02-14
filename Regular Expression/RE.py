import re
l=re.finditer("[^abc]","absdf123bsd")
for p in l:
    print(p.start(),"...",p.end(),"...",p.group())