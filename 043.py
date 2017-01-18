#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
43. 名詞を含む文節が動詞を含む文節に係るものを抽出

名詞を含む文節が，動詞を含む文節に係るとき，
これらをタブ区切り形式で抽出せよ．
"""

import sys

from section5 import *

# Chunk に追加
#
# def contains(self, attr, query):
#     return any(m[attr] == query for m in self.morphs)

def main():
    for sentence in parse_cabocha(sys.stdin):
        for path in sentence.connect_path():
            if (path[0].contains('pos', '名詞') and
                path[1].contains('pos', '動詞')):
                print '\t'.join(path.surfaces())

# どこで  生れたか
# 見当が  つかぬ
# 所で    泣いていた
# ニャーニャー    泣いていた
# 事だけは        記憶している

# %timeit !src/043.py < data/neko.txt.cabocha > /dev/null
# 1 loops, best of 3: 970 ms per loop

if __name__ == '__main__':
    main()
