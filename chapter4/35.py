#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from functions import read_results

results = read_results()
noun = []
for lines in results:
    cnt = 0
    seq = ""
    for line in lines:
        if "名詞" in line['pos']:
            cnt += 1
            seq += line["surface"]
        else:
            if cnt > 1:
                noun.append(seq)
            cnt = 0
            seq = ""

print(noun)
