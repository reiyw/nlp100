#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""33. サ変名詞

30で作成したプログラムを活用し，サ変接続の名詞をすべて抽出せよ．
"""


import sys

import p030


def main():
    for sentence in p030.parse_mecab_seq(sys.stdin):
        for morph in sentence:
            if morph['pos1'] == 'サ変接続':
                print morph['base']

# 見当
# 記憶
# 話
# 装飾
# 突起

if __name__ == '__main__':
    main()
