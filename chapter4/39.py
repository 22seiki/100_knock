#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from functions import read_results
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

fp = FontProperties(fname='./IPAexfont00301/ipaexg.ttf')

results = read_results()
frq = Counter()
for lines in results:
    lists = []
    for line in lines:
        lists.append(line["surface"])
    frq += Counter(lists)

X = []
Y = []
i = 0
for word, cnt in frq.most_common():
    X.append(i)
    Y.append(cnt)
    i += 1

plt.scatter(range(len(Y)), Y)
plt.xscale('log')
plt.yscale('log')
plt.xlim(1, len(Y))
plt.ylim(1, len(X))
plt.xlabel('出現度順位', fontproperties=fp)
plt.ylabel('出現頻度', fontproperties=fp)
plt.show()
