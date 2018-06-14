#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from functions import read_results

results = read_results()
noun = []
for lines in results:
    for i, line in enumerate(lines):
        if "の" == line['surface'] and "助詞" in line['pos']:
            if "名詞" == lines[i-1]["pos"] and "名詞" == lines[i+1]["pos"]:
                noun.append(lines[i-1]["surface"] +
                            line["surface"] + lines[i+1]["surface"])

print(noun)
