#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re

with open("./jawiki-country.json", 'r') as f:
    dic = {i: json.loads(line) for i, line in enumerate(f)}

for k in dic.keys():
    if u"イギリス" in dic[k]["title"]:
        text = dic[k]["text"]

lists = {}
for i, line in enumerate(text.split("\n")):
    # print(i, line)
    if re.match(r'\|(\w*\s=\s.*)', line):
        template = re.search(r'\|(\w*)', line).group()
        template = re.sub(r'^\|', "", template)
        lists[template] = re.search(r'.*\s=\s(.*)', line).group()
        lists[template] = re.sub(r'.*\s=\s', "", lists[template])
    elif re.match(r'\*+\{\{lang.*', line):
        lists[template] += re.search(r'\*+\{\{lang.*', line).group()

for k, v in lists.items():
    if re.match(r'.*\'{3}', v):
        v = re.sub(r'\'{3}', "", v)
    if re.match(r'.*\[{2}', v):
        v = re.sub(r'(\[|\]){2}', "", v)
    print(k, v)
