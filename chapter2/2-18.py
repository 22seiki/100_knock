#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import itemgetter
import re

with open('hightemp.txt', 'r') as f:
    text = f.readlines()

lines = []
for line in text:
    lines.append(line.split("\t"))
lines.sort(key=itemgetter(2), reverse=True)

text_sort = ""
for len in lines:
    for wd in len:
        wd = re.sub(r'\n', "\t", wd)
        text_sort += wd + "\t"
    text_sort += "\n"
print(text_sort)
