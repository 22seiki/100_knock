#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

with open('col1.txt', 'r') as f:
    col1 = f.read()
with open('col2.txt', 'r') as f:
    col2 = f.read()

col1 = re.sub(r'\n', "", col1)
merge = col1 + "\t" + col2

with open('merge.txt', 'w') as f:
    f.write(merge)
