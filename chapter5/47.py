#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
import sys
import re
from functions import Chunk


def make_sentences(text):
    lines = []
    sentences = []
    global pos_list
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
            if lines['pos1'] == 'サ変接続':
                lines['surface'] = re.sub("[。|、|\s]", "", lines['surface'])
                s = {lines['pos1']: lines['surface']}
            elif lines['pos'] == '動詞':
                lines['base'] = re.sub("[。|、|\s]", "", lines['base'])
                s = {lines['pos']: [lines['surface'], lines['base']]}
            else:
                lines['surface'] = re.sub("[。|、|\s]", "", lines['surface'])
                s = {lines['pos']: lines['surface']}
            chunk.morphs[id].append(s)
            if chunk.dst != -1 and id not in chunk.srcs[chunk.dst]:
                chunk.srcs[chunk.dst].append(id)
    return chunk


def make_paterns(morph1, morph2, morph3):
    paterns = []
    for i, s_dic in enumerate(morph1):
        if i+1 < len(morph1):
            if 'サ変接続' in s_dic and '助詞' in morph1[i+1] and\
               morph1[i+1]['助詞'] == 'を':
                for vdic in morph2:
                    if '動詞' in vdic:
                        s = s_dic['サ変接続'] + morph1[i+1]['助詞']\
                            + vdic['動詞'][1] + '\t'
                        s2 = ''
                        sv = ''
                        flag = False
                        for dic in morph3:
                            if '動詞' not in dic:
                                l = list(dic.values())
                                sv += l[0]
                            else:
                                sv += dic['動詞'][0]
                            if '助詞' in dic:
                                s += dic['助詞'] + ' '
                                s2 += sv + ' '
                                sv = ''
                                flag = True
                        s += '\t' + s2
                        if flag:
                            paterns.append(s)
    return paterns


def adjust_list(paterns):
    regex = r'\t.+'
    subst = re.compile(regex)
    vlist = []
    list = []
    for patern in paterns:
        if subst.sub('', patern) not in vlist:
            vlist.append(subst.sub('', patern))
            list.append(patern)
        else:
            if patern in list:
                print(vlist, patern, list)
            else:
                print(patern, list)
                sys.exit()
    return list


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
                for dic in chunk.morphs[i]:
                    paterns = make_paterns(chunk.morphs[i-1],
                                           chunk.morphs[i],
                                           chunk.morphs[id])
                    paterns = adjust_list(paterns)
                    for patern in paterns:
                        v_sentenses.append(patern)
    counter = collections.Counter(v_sentenses)
    lines = ''
    for k in counter.keys():
        lines += k + '\n'
    with open('47result.txt', 'w') as f:
        f.write(lines)
