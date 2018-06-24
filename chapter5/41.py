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


class Chunk:
    def __init__(self):
        self.morphs = []
        self.dst = 0
        self.srcs = []

    def __call__(self, sentence):
        self.srcs = [[] for i in range(len(sentence))]


if __name__ == '__main__':
    path = "./neko.txt.cabocha"
    with open(path, "r") as f:
        txt = str(f.read())
    lines = []
    sentences = []
    for line in txt.split("\n"):
        line = re.sub("[,|\t]", " ", line)
        lists = list(line.split(" "))
        if len(lists) > 5 and "EOS" not in lists:
            dic = {
                "surface": lists[0],
                "base": lists[7],
                "pos": lists[1],
                "pos1": lists[2]
            }
            lines.insert(i, dic)
            i += 1
        elif "EOS" not in lists:
            i = len(lines)
            lines.append(lists)
        if "EOS" in lists:
            sentences.append(lines)
            lines = []

    for i, sentence in enumerate(sentences):
        chunk = Chunk()
        chunk(sentence)
        s = ""
        tmp = 0
        for lines in sentence:
            if isinstance(lines, list):
                lines[2] = re.sub("D", "", lines[2])
                chunk.dst = int(lines[2])
                chunk.morphs.append(s)
                chunk.srcs[chunk.dst].append(int(lines[1]))
                s = ""
                if i == 7:
                    print(chunk.morphs[tmp], chunk.dst, chunk.srcs[tmp])
                    tmp += 1
            else:
                s += lines["surface"]
