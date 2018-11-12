#!/usr/bin/env python
import xml.etree.ElementTree as ET


def main():
    tree = ET.parse('nlp.txt.xml')
    root = tree.getroot()

    element = './document/sentences/sentence'

    for sentence in root.findall(element):
        for tokens in sentence:
            if tokens.tag == 'dependencies':
                continue
            for token in tokens:
                txt = ''
                for t in token:
                    if t.tag == 'word':
                        txt += t.text
                    if t.tag == 'NER' and t.text == 'PERSON':
                        print(txt)


if __name__ == '__main__':
    main()
