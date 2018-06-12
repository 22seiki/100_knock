#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
path = './neko.txt.mecab'

with open(path) as f:
    txt = str(f.read())

surface = []
base = []
pos = []
pos1 = []
for line in txt.split("\n"):
    line = re.sub(",", " ", line)
    lists = list(line.split())
    for j, v in enumerate(lists):
        if j == 0:
            surface.append(v)
        elif j == 1:
            pos.append(v)
        elif j == 2:
            pos1.append(v)
        elif j == 7:
            base.append(v)

values = []
values.append(surface)
values.append(base)
values.append(pos)
values.append(pos1)

keys = ['surface', 'base', 'pos', 'pos1']
dic = {}
for k, v in zip(keys, values):
    dic[k] = values

print(dic['surface'])
