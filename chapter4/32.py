#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from functions import read_results

results = read_results()
base = []
for lines in results:
    for line in lines:
        if "動詞" in line['pos']:
            base.append(line['base'])

print(base)
