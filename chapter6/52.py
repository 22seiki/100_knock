#!/usr/bin/env python
# -*- coding: utf-8 -*-
from nltk import stem
from function import text_wd


def main():
    stemmer = stem.PorterStemmer()
    wd_list = text_wd()

    for wd in wd_list:
        print('{0}\t{1}'.format(wd, stemmer.stem(wd)))

if __name__ == '__main__':
    main()
