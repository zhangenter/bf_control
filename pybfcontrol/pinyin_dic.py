# -*- coding=utf-8 -*-
from pypinyin import pinyin, lazy_pinyin, Style
import codecs
start,end = (0x4E00, 0x9FA5)
d = {}
for codepoint in range(int(start),int(end)):
    w = unichr(codepoint)
    arr = pinyin(w, style=Style.TONE3, heteronym=True)[0]
    arr = set(map(lambda t:t[:-1],arr))
    for x in arr:
    	if x in d: d[x].append(w)
    	else: d[x] = [w]
    # if len(d)>1000:
    # 	break
import json
f=file('pinyin.json', 'w+')
json.dump(d,f)
f.close()