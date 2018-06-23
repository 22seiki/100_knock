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

    def analysis(self, sentences):
        for line in sentences:
            self.surface = line["surface"]
            self.base = line["base"]
            self.pos = line["pos"]
            self.pos1 = line["pos1"]


class Chunk():
    def __init__(self):
        self.morphs = []
        self.dst = 0
        self.srcs = []

    def chunk(self, sentences):
        s = ""
        for line in sentences:
            # print(line)
            if isinstance(line, list):
                self.morphs.append(s)
                self.srcs.append([])
                s = ""
            else:
                s += line["surface"]
        self.morphs.append(s)
        for line in sentences:
            if isinstance(line, list):
                line[2] = re.sub("D", "", line[2])
                self.dst = int(line[2])
                if self.dst != -1:
                    self.srcs[self.dst].append(int(line[1]))
                i = int(line[1]) + 1
