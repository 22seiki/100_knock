#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
from functions import Chunk, Morph

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

    for sentence in sentences:
        chunk = Chunk()
        chunk(sentence)
        s = ''
        lists = []
        for lines in sentence:
            if isinstance(lines, list):
                lines[2] = re.sub("D", "", lines[2])
                chunk.dst = int(lines[2])
                s = re.sub("[。|、|\s]", "", s)
                if '動詞' in lists:
                    chunk.morphs.append(s)
                elif '名詞' in lists:
                    chunk.morphs.append(s)
                    if chunk.dst != -1:
                        chunk.srcs[chunk.dst].append(int(lines[1]))
                else:
                    chunk.morphs.append('')
                s = ''
                lists = []
            else:
                lists.append(lines['pos'])
                s += lines["surface"]
        for i, src in enumerate(chunk.srcs):
            if src == []:
                continue
            if len(src) > 1:
                for idx in src:
                    if chunk.morphs[idx] != "":
                        print("{0}\t{1}".format(chunk.morphs[idx],
                                                chunk.morphs[i]))
            else:
                if chunk.morphs[src[0]] != "":
                    print("{0}\t{1}".format(chunk.morphs[src[0]],
                                            chunk.morphs[i]))
