#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""29. 国旗画像のURLを取得する

テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki
APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
"""

import sys
import json

import httplib2


def main():
    info_dict = json.loads(sys.stdin.read())
    query = httplib2.urllib.urlencode({
        'format': 'json',
        'action': 'query',
        'prop': 'imageinfo',
        'iiprop': 'url',
        'titles': 'Image:{}'.format(info_dict[u'国旗画像']),
    })
    h = httplib2.Http('.cache')
    response, content = h.request(
        'http://en.wikipedia.org/w/api.php?{}'.format(query))

    for page in json.loads(content)['query']['pages'].itervalues():
        print page['imageinfo'][0]['url']

# http://upload.wikimedia.org/wikipedia/en/a/ae/Flag_of_the_United_Kingdom.svg

if __name__ == '__main__':
    main()
