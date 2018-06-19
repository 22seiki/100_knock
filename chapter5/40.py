#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


class Morph:
    def __init__(self):
        self.surface = ""
        self.base = ""
        self.pos = ""
        self.pos1 = ""
        self.sentences = []

    def divide(self, txt):
        lines = []
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
                self.sentences.append(lines)
                lines = []

    def analysis(self, i=0):
        print(self.sentences[i])
        for line in self.sentences[i]:
            self.surface = line["surface"]
            self.base = line["base"]
            self.pos = line["pos"]
            self.pos1 = line["pos1"]
            print(self.surface, self.base, self.pos, self.pos1)


if __name__ == '__main__':
    morph = Morph()
    path = "./neko.txt.cabocha"
    with open(path, "r") as f:
        txt = str(f.read())
    morph.divide(txt)
    morph.analysis(2)
