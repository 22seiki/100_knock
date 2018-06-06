#!/usr/bin/env python
# -*- coding: utf-8 -*-
with open('hightemp.txt', 'r') as f:
    text = f.readlines()

raw1 = []
for line in text:
    if not line.split("\t")[0] in raw1:
        raw1.append(line.split("\t")[0])

raw1.sort()
raw1.sort(key=len)
raw = ""
for line in raw1:
    if line != " ":
        raw += line + "\n"
print(raw)
