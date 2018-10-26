#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


def text_br(text):
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


def text_not_br(text):
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


def main():
    with open('nlp.txt', 'r') as f:
        text = f.read()

    text = text_br(text)

    txt = ''

    pattern = r'[\.|:|;|\?|\!]'
    repattern = re.compile(pattern)

    for wd1, wd2 in zip(text.split(' '), text.split(' ')[1:]):
        if len(wd1) == 0:
            continue
        if repattern.match(wd1):
            # print("wd1 = ", wd1)
            if not wd2.islower() and not repattern.match(wd2):
                txt += wd1
                print(text_not_br(txt))
                txt = ''
            else:
                txt += wd1 + ' '
        else:
            txt += wd1 + ' '


if __name__ == '__main__':
    main()
