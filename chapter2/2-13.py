#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

with open('col1.txt', 'r') as f:
    col1 = f.readlines()
with open('col2.txt', 'r') as f:
    col2 = f.readlines()

merge = ""
idx = 0
for wd1 in col1:
    wd1 = re.sub(r'\n', "\t", wd1)
    merge += wd1 + col2[idx]
    idx += 1

with open('merge.txt', 'w') as f:
    f.write(merge)
