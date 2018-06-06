#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

with open('hightemp.txt', 'r') as f:
    text = f.readline()

for s in text.split('\t'):
    print(s)
