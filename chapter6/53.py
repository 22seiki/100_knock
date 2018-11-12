#!/usr/bin/env python
import xml.etree.ElementTree as ET


def main():
    # ファイルの内容でtreeを初期化
    tree = ET.ElementTree(file='nlp.txt.xml')

    # treeのroot要素を取得
    root = tree.getroot()

    element = './document/sentences/sentence/tokens/token/word'

    for word in root.findall(element):
        print(word.text)

if __name__ == '__main__':
    main()
