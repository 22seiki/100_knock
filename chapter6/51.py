#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from function import text_format


def wd_format(wd):
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


def main():
    text = text_format()

    for txt in text.split('\n'):
        for wd in txt.split(' '):
            print(wd_format(wd))
        print(' ')

if __name__ == '__main__':
    main()
