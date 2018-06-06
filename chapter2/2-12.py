#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('hightemp.txt', 'r') as f:
    text = f.readlines()

prefecture = ""
city = ""
for line in text:
    raw = 0
    for wd in line.split("\t"):
        if raw == 0:
            prefecture += (wd + "\n")
        elif raw == 1:
            city += (wd + "\n")
        raw += 1

with open('col1.txt', 'w') as f:
    f.write(prefecture)
with open('col2.txt', 'w') as f:
    f.write(city)
