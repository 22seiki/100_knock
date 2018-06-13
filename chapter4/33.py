#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from functions import read_results

results = read_results()
surface = []
for lines in results:
    for line in lines:
        if "サ変接続" in line['pos1'] and "名詞" in line['pos']:
            surface.append(line['surface'])

print(surface)
