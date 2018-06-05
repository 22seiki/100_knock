#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

with open('hightemp.txt', 'r') as f:
    text = []
    for line in f.readlines():
        text.append(re.sub(r'\n', "", line))

n = int(input())
cnt = 0
for line in text:
    cnt += 1
    print(line)
    if cnt == n:
        print('\n')
        cnt = 0
