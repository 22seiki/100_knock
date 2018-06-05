#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('hightemp.txt', 'r') as f:
    text = f.read()

prefecture = ""
city = ""
raw = 0
for wd in text.split('\t' | '\n'):
    print(wd)
    if raw == 0:
        prefecture += wd + "\n"
    elif raw == 1:
        city += wd + "\n"
    elif raw == 3:
        raw = 0
    else:
        raw += 1
print(prefecture)
with open('col1.txt', 'w') as f:
    f.write(text[0])
with open('col2.txt', 'w') as f:
    f.write(text[1])
