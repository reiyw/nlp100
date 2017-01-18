#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""27. 内部リンクの除去

26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを
除去し，テキストに変換せよ（参考:
http://ja.wikipedia.org/wiki/Help:%E6%97%A9%E8%A6%8B%E8%A1%A8 ）．
"""


import sys
import re
import json


def main():
    info_dict = json.loads(sys.stdin.read())
    for k, v in info_dict.iteritems():
        info_dict[k] = re.sub(r'\[\[.*?([^|]+?)\]\]', r'\1', v)

    if len(sys.argv) > 1:
        for k, v in info_dict.iteritems():
            print u'{} = {}'.format(k, v)
    else:
        sys.stdout.write(json.dumps(info_dict))

# 公式国名 = {{lang|en|United Kingdom of Great Britain and Northern Ireland}}<ref>英語以外での正式国名:<br/>
# ccTLD = .uk / .gb<ref>使用は.ukに比べ圧倒的少数。</ref>
# 首都 = ロンドン
# GDP値 = 2兆3162億<ref name="imf-statistics-gdp" />
# 確立形態4 = 現在の国号「グレートブリテン及び北アイルランド連合王国」に変更

if __name__ == '__main__':
    main()
