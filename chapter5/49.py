#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from functions import Chunk
n_dic = {}


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
    n_dic = {}
    chunk = Chunk()
    chunk(sentence)
    s = ""
    ns = ''
    flag = False
    nlists = []
    for lines in sentence:
        if isinstance(lines, list):
            lines[2] = re.sub("D", "", lines[2])
            chunk.dst = int(lines[2])
            s = re.sub("[。|、|\s]", "", s)
            chunk.morphs.append(s)
            if chunk.dst != -1:
                chunk.srcs[chunk.dst].append(int(lines[1]))
            if flag:
                n_dic[s] = nlists
                flag = False
            s = ""
            nlists = []
        else:
            s += lines["surface"]
            if lines['pos'] == '名詞':
                flag = True
                nlists.append(lines['surface'])
    return chunk


def make_path(chunk, path, id, end, lists):
    if chunk.srcs[id] == [] and end not in lists:
        path.pop(len(path)-1)
        make_path(chunk, path, chunk.dst, end, lists)
    for i in chunk.srcs[id]:
        if i not in lists and end not in lists:
            path.append(chunk.morphs[i] + ' -> ')
            lists.append(i)
            make_path(chunk, path, i, end, lists)
    return path


def path_extraction(chunk, paths):
    morphs = []
    for i in range(len(chunk.morphs)):
        if i < len(chunk.morphs) - 1:
            s = chunk.morphs[i] + ' -> '
        else:
            s = chunk.morphs[i]
        morphs.append(s)
    dic = {}
    print(morphs, n_dic, paths)
    for i, morph in enumerate(morphs):
        if i == 0:
            s = ''
            flag = False
        if morph.strip(' -> ') not in n_dic.keys():
            for path in paths:
                if morph in path:
                    s += morph
                    break
            if morphs[len(morphs)-1] in s and not flag:
                print(s2)
            continue
        for k, v in n_dic.items():
            if k in morphs[i]:
                for v2 in v:
                    if v2 in morphs[i]:
                        if 'X' not in s:
                            s += 'X' + morphs[i].strip(v2)
        # print(s)
        for j in range(i+1, len(morphs)):
            for path in paths:
                s2 = s.strip(' -> ')
                # print(s2)
                if morphs[j:len(morphs)] == path\
                   and path not in dic.values():
                    dic[j] = path
                    s2 += ' | '
                    for k, v in n_dic.items():
                        if path[0].strip(' -> ') in k:
                            for v2 in v:
                                if v2 in path[0]:
                                    s2 += 'Y' + path[0].strip(v2)
                    if len(path) > 2:
                        for k in range(1, len(path)-1):
                            if k < len(path) - 2:
                                s2 += path[k]
                            else:
                                s2 += path[k].strip(' -> ')
                    else:
                        s2 = s2.strip(' -> ')
                    s2 += ' | ' + morphs[len(morphs)-1]
                    print(s2)
                    flag = True
    for i, path in enumerate(paths):
        if path not in dic.values():
            dic[len(paths)+i] = path
    for v in dic.values():
        i = 1
        p = v[0:len(v)]
        for k, n in n_dic.items():
            if p[0].strip(' -> ') == k:
                for v in n:
                    if v in p[0]:
                        s = 'X' + p[0].strip(v)
                for i in range(1, len(p)):
                    for k in n_dic.keys():
                        # print(p[i], k)
                        if p[i].strip(' -> ') == k:
                            print(s + 'Y')
                            break
                    s += p[i]


if __name__ == '__main__':
    path = "./neko.txt.cabocha"
    with open(path, "r") as f:
        txt = str(f.read())
    sentences = make_sentences(txt)
    j = 0
    for sentence in sentences:
        chunk = make_chunk(sentence)
        paths = []
        repaths = []
        for i in range(len(chunk.morphs)-1, 0, -1):
            if chunk.morphs[len(chunk.morphs)-i-1] not in n_dic.keys():
                continue
            chunk.dst = len(chunk.morphs)-1
            l = [chunk.morphs[len(chunk.morphs)-1]]
            path = make_path(chunk, l, len(chunk.morphs)-1,
                             len(chunk.morphs)-i-1,
                             [len(chunk.morphs)-1])
            repath = []
            for v in reversed(path):
                repath.append(v)
            paths.append(repath)
        if j == 5:
            path_extraction(chunk, paths)
        j += 1
