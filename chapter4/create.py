#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MeCab

path = './neko.txt'
mecab = MeCab.Tagger('-Ochasen')

with open(path) as f:
    txt = f.read()

malist = mecab.parse(txt)

with open("neko.txt.mecab", "w") as f:
    f.write(malist)
