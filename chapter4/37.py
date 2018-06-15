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

i = 0
X = []
Y = []
xlabel = []
for word, cnt in frq.most_common():
    xlabel.append(word)
    X.append(i)
    Y.append(cnt)
    i += 1
    if i == 10:
        break

plt.xticks(X, xlabel, fontproperties=fp)
plt.bar(X, Y, align='center')
plt.show()
