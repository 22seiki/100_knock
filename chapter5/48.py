#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from functions import Chunk
n_dic = []
n_flag = False


def make_sentences(filename):
    lines = []
    sentences = []
    for line in filename.split("\n"):
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
    return sentences


def make_chunk(sentence):
    global n_dic
    n_dic = []
    chunk = Chunk()
    chunk(sentence)
    s = ""
    flag = False
    for lines in sentence:
        if isinstance(lines, list):
            lines[2] = re.sub("D", "", lines[2])
            chunk.dst = int(lines[2])
            s = re.sub("[。|、|\s]", "", s)
            chunk.morphs.append(s)
            if chunk.dst != -1:
                chunk.srcs[chunk.dst].append(int(lines[1]))
            if flag:
                n_dic.append(s)
                flag = False
            s = ""
        else:
            s += lines["surface"]
            if lines['pos'] == '名詞':
                flag = True
    return chunk


def make_path(chunk, path, id, end, lists):
    global n_flag
    if chunk.srcs[id] == [] and end not in lists:
        path.pop(len(path)-1)
        make_path(chunk, path, chunk.dst, end, lists)
    for i in chunk.srcs[id]:
        if end in lists:
            break
        if i not in lists:
            path.append(chunk.morphs[i] + ' -> ')
            lists.append(i)
            if chunk.morphs[i] in n_dic:
                n_flag = True
            make_path(chunk, path, i, end, lists)
    if n_flag:
        return path
    else:
        return []


if __name__ == '__main__':
    path = "./neko.txt.cabocha"
    with open(path, "r") as f:
        txt = str(f.read())
    sentences = make_sentences(txt)
    j = 0
    for sentence in sentences:
        chunk = make_chunk(sentence)
        for i in range(len(chunk.morphs)-1, 0, -1):
            chunk.dst = len(chunk.morphs)-1
            l = [chunk.morphs[len(chunk.morphs)-1]]
            if j == 7:
                n_flag = False
                path = make_path(chunk, l, len(chunk.morphs)-1,
                                 len(chunk.morphs)-i-1, [])
                s = ''
                for v in reversed(path):
                    s += v
                print(s)
        j += 1
