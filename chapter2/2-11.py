#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

with open('hightemp.txt', 'r') as f:
    text = f.read()
text = re.sub('\t', " ", text)
print(text)
