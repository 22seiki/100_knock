#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re
import requests


def json_search(json_data):
    json_dic = {}
    for k, v in json_data.items():
        if isinstance(v, list):
            for e in v:
                json_dic.update(json_search(e))
        elif isinstance(v, dict):
            json_dic.update(json_search(v))
        else:
            json_dic[k] = v
    return json_dic

if __name__ == '__main__':
    with open("./jawiki-country.json", 'r') as f:
        dic = {i: json.loads(line) for i, line in enumerate(f)}

    for k in dic.keys():
        if u"イギリス" in dic[k]["title"]:
            text = dic[k]["text"]

    lists = {}
    for i, line in enumerate(text.split("\n")):
        # print(i, line)
        if re.match(r'\|(\w*\s=\s.*)', line):
            template = re.search(r'\|(\w*)', line).group()
            template = re.sub(r'^\|', "", template)
            lists[template] = re.search(r'.*\s=\s(.*)', line).group()
            lists[template] = re.sub(r'.*\s=\s', "", lists[template])
        elif re.match(r'\*+\{\{lang.*', line):
            lists[template] += re.search(r'\*+\{\{lang.*', line).group()

    url = "https://en.wikipedia.org/w/api.php"
    payload = {"action": "query",
               "titles": "File:{}".format(lists[u"国旗画像"]),
               "prop": "imageinfo",
               "format": "json",
               "iiprop": "url"}

    json_data = requests.get(url, params=payload).json()
    # print(json_data)
    print(json_search(json_data)['url'])
