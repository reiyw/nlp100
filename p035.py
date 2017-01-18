#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""35. 名詞の連接

名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
"""

import sys
import itertools

import p030


def main():
    for sentence in p030.parse_mecab_seq(sys.stdin):
        for key, group in itertools.groupby(sentence, key=lambda m: m['pos']):
            if key == '名詞':
                noun_conjunction = [m['surface'] for m in group]
                if len(noun_conjunction) > 1:
                    print ''.join(noun_conjunction)

# 人間中
# 一番獰悪
# 時妙
# 一毛
# その後猫

if __name__ == '__main__':
    main()
