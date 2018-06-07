#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

with open("./jawiki-country.json", 'r') as f:
    dic = {i: json.loads(line) for i, line in enumerate(f)}

for k in dic.keys():
    if u"イギリス" in dic[k]["title"]:
        text = dic[k]["text"]

print(text)
