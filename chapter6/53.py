#!/usr/bin/env python
import xml
from function import text_format


def main():
    txt = text_format()
    nlp = StanfordCoreNLP('http://localhost:9000')
    output = nlp.annotate(txt, properties=)
    print(output)

if __name__ == '__main__':
    main()
