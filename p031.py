#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""31. 動詞

動詞の表層形をすべて抽出せよ．
"""

import sys

import p030


def main():
    for sentence in p030.parse_mecab_seq(sys.stdin):
        for morph in sentence:
            if morph['pos'] == '動詞':
                print morph['surface']

# 生れ
# つか
# し
# 泣い
# い

if __name__ == '__main__':
    main()
