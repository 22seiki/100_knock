#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
import sys
import re
from functions import Chunk, Morph


def make_sentences(text):
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
            morph = Morph(dic['surface'], dic['base'], dic['pos'], dic['pos1'])
            if '動詞' == morph.pos or '助詞' == morph.pos:
                lines.append(dic)
        elif "EOS" not in lists:
            lines.append(lists)
        if "EOS" in lists:
            sentences.append(lines)
            lines = []
    return sentences


def make_chunk(sentence):
    chunk = Chunk()
    chunk(sentence)
    for lines in sentence:
        if isinstance(lines, list):
            s = {}
            lines[2] = re.sub("D", "", lines[2])
            chunk.dst = int(lines[2])
            id = int(lines[1])
            chunk.morphs.append([])
        else:
            lines['base'] = re.sub("[。|、|\s]", "", lines['base'])
            s = {lines['pos']: lines['base']}
            chunk.morphs[id].append(s)
            if chunk.dst != -1 and id not in chunk.srcs[chunk.dst]:
                chunk.srcs[chunk.dst].append(id)
    return chunk


def make_paterns(morph1, morph2):
    paterns = []
    flag = False
    for vdic in morph1:
        if '動詞' in vdic:
            s = vdic['動詞'] + '\t'
            for dic in morph2:
                if '助詞' in dic:
                    s += dic['助詞'] + ' '
                    flag = True
            if flag:
                paterns.append(s)
    return paterns


if __name__ == '__main__':
    path = "./neko.txt.cabocha"
    with open(path, "r") as f:
        txt = str(f.read())
    sentences = make_sentences(txt)
    v_sentenses = []
    for sentence in sentences:
        chunk = make_chunk(sentence)
        for i, src in enumerate(chunk.srcs):
            if [] == src:
                continue
            for id in src:
                paterns = make_paterns(chunk.morphs[i], chunk.morphs[id])
                for patern in paterns:
                    v_sentenses.append(patern)
    counter = collections.Counter(v_sentenses)
    lines = ''
    for k in counter.keys():
        lines += k + '\n'
    with open('45result.txt', 'w') as f:
        f.write(lines)
