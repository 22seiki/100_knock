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
        self.srcs = [[] for lists in sentence if isinstance(lists, list)]

    def __str__(self):
        return "{0} {1} {2}".format(self.morphs, self.dst, self.srcs)
