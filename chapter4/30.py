#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
path = './neko.txt.mecab'

with open(path) as f:
    txt = str(f.read())


def read_results():
    lines = []
    for line in txt.split("\n"):
        line = re.sub(",", " ", line)

        if 'EOS' in line:
            continue
        lists = list(line.split())
        dic = {}
        for j, v in enumerate(lists):
            if j == 0:
                dic["surface"] = v
            if j == 1:
                dic["pos"] = v
            if j == 2:
                dic["pos2"] = v
            if j == 7:
                dic["base"] = v
        lines.append(dic)

        if "。" in dic.values():
            print(lines)
            lines = []

if __name__ == '__main__':
    read_results()
