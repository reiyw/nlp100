#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""32. 動詞の原形

動詞の原形をすべて抽出せよ．
"""

import sys

import p030


def main():
    for sentence in p030.parse_mecab_seq(sys.stdin):
        for morph in sentence:
            if morph['pos'] == '動詞':
                print morph['base']

# 生れる
# つく
# する
# 泣く
# いる

if __name__ == '__main__':
    main()
