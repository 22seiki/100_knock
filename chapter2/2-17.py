#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

with open('hightemp.txt', 'r') as f:
    text = f.readlines()

raw1 = []
for line in text:
    if not line.split("\t")[0] in raw1:
        raw1.append(line.split("\t")[0])
print("和歌山県" > "千葉県")
raw1.sort()
raw = ""
for line in raw1:
    if line != " ":
        raw += line + "\n"
print(raw)
