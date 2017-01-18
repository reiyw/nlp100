#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""25. テンプレートの抽出

記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
辞書オブジェクトとして格納せよ．
"""

import sys
import re
import json


def main():
    info_dict = dict()
    for line in sys.stdin:
        if line.startswith('{{基礎情報'):
            for inner_line in sys.stdin:
                for m in re.finditer(r'\|(.+?)\s*=\s*(.+?)\s*$', inner_line):
                    info_dict[m.group(1)] = m.group(2)
                if inner_line.startswith('}}'):
                    break
            break

    if len(sys.argv) > 1:
        for key, value in info_dict.iteritems():
            print '{key} = {value}'.format(key=key, value=value)
    else:
        sys.stdout.write(json.dumps(info_dict))

# 公式国名 = {{lang|en|United Kingdom of Great Britain and Northern Ireland}}<ref>英語以外での正式国名:<br/>
# ccTLD = [[.uk]] / [[.gb]]<ref>使用は.ukに比べ圧倒的少数。</ref>
# 首都 = [[ロンドン]]
# GDP値 = 2兆3162億<ref name="imf-statistics-gdp" />
# 確立形態4 = 現在の国号「'''グレートブリテン及び北アイルランド連合王国'''」に変更


if __name__ == '__main__':
    main()
