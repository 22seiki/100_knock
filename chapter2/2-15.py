#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

with open('hightemp.txt', 'r') as f:
    text = []
    for line in f.readlines():
        text.append(re.sub(r'\n', "", line))

n = int(input())
for i in range(n, 0, -1):
    print(text[len(text) - i])
