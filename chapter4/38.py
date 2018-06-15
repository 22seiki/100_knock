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

Y = []
for word, cnt in frq.most_common():
    Y.append(cnt)

plt.xlabel('出現頻度', FontProperties=fp)
plt.ylabel('単語の種類数', fontproperties=fp)
plt.grid(axis='y')
plt.xlim(xmin=1, xmax=20)
plt.hist(Y, bins=30, range=(1, 30))
plt.show()
