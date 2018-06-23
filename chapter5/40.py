#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return "{0} {1} {2} {3}"\
            .format(self.surface, self.base, self.pos, self.pos1)


if __name__ == '__main__':
    path = "./neko.txt.cabocha"
    with open(path, "r") as f:
        txt = str(f.read())
    lines = []
    sentences = []
    for line in txt.split("\n"):
        line = re.sub("[,|\t]", " ", line)
        lists = list(line.split(" "))
        if len(lists) < 6 and "EOS" not in lists:
            continue
        if "EOS" not in lists:
            dic = {
                "surface": lists[0],
                "base": lists[7],
                "pos": lists[1],
                "pos1": lists[2]
            }
            lines.append(dic)
        else:
            sentences.append(lines)
            lines = []

    for i, sentence in enumerate(sentences):
        if i == 2:
            for lists in sentence:
                print(Morph(lists["surface"], lists["base"],
                            lists["pos"], lists["pos1"]))
