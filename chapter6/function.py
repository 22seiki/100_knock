#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


def _text_br(text):
    dic = {
        '.': ' .',
        ':': ' :',
        ';': ' ;',
        '?': ' ?',
        '!': ' !',
        '\n': ' ',
    }

    for k, v in dic.items():
        text = text.replace(k, v)

    return text


def _text_not_br(text):
    dic = {
        ' .': '.',
        ' :': ':',
        ' ;': ';',
        ' ?': '?',
        ' !': '!',
    }

    for k, v in dic.items():
        text = text.replace(k, v)

    return text


def _wd_format(wd):
    pattern = r'[\.|:|;|\?|\!|,|\"|\'|\(|\)|\[|\]]'
    repattern = re.compile(pattern)

    if len(repattern.findall(wd)) == 1:
        wd = repattern.sub('', wd)
    elif len(repattern.findall(wd)) > 1:
        wd = re.sub(r'[\"|\'|\(|\)|\[|\]]', '', wd)
        if len(re.findall('\.', wd)) > 1:
            wd = re.sub(r'[\?|\!|:|;|,]', '', wd)
        else:
            wd = repattern.sub('', wd)
    return wd


def text_format():
    with open('nlp.txt', 'r') as f:
        text = f.read()

    text = _text_br(text)

    txt = ''

    pattern = r'[\.|:|;|\?|\!]'
    repattern = re.compile(pattern)

    for wd1, wd2 in zip(text.split(' '), text.split(' ')[1:]):
        if len(wd1) == 0:
            continue
        if repattern.match(wd1):
            # print("wd1 = ", wd1)
            if not wd2.islower() and not repattern.match(wd2):
                txt += wd1 + '\n'
                txt = _text_not_br(txt)
            else:
                txt += wd1 + ' '
        else:
            txt += wd1 + ' '
    return txt


def text_wd():
    text = text_format()
    wd_list = []

    for txt in text.split('\n'):
        for wd in txt.split(' '):
            wd_list.append(_wd_format(wd))
        wd_list.append(' ')

    return wd_list

if __name__ == '__main__':
    main()
