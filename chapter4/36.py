#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from functions import read_results
from collections import Counter

results = read_results()
frq = Counter()
for lines in results:
    lists = []
    for line in lines:
        lists.append(line["surface"])
    frq += Counter(lists)

dic = {}
for word, cnt in frq.most_common():
    dic[word] = cnt

print(dic)
