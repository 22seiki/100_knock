#!/usr/bin/env python
# -*- coding: utf-8 -*-
from operator import itemgetter

with open('hightemp.txt', 'r') as f:
    text = f.readlines()

frq = {}
for line in text:
    raw = 0
    for wd in line.split("\t"):
        if raw == 0:
            if wd in frq:
                frq[wd] += 1
            else:
                frq[wd] = 1
        raw += 1

dic = {}
for k, v in sorted(frq.items(), key=lambda x: x[1], reverse=True):
    dic[k] = v

text_sort = ""
for k in dic.keys():
    for line in text:
        if k in line:
            text_sort += line

print(text_sort)
