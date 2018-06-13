#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


def read_results():
    path = './neko.txt.mecab'
    with open(path) as f:
        txt = str(f.read())

    lines = []
    results = []
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
                dic["pos1"] = v
            if j == 7:
                dic["base"] = v
        lines.append(dic)

        if "。" in dic.values():
            results.append(lines)
            lines = []
    return results

if __name__ == '__main__':
    results = read_results()
    for line in results:
        print(line)
