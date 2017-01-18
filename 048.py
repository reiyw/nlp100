#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
48. 名詞から根へのパスの抽出

文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ．
ただし，構文木上のパスは以下の仕様を満たすものとする．

- 各文節は（表層形の）形態素列で表現する
- パスの開始文節から終了文節に至るまで，各文節の表現を"->"で連結する

「吾輩はここで始めて人間というものを見た」という文（neko.txt.cabochaの8文目）
から，次のような出力が得られるはずである．

  吾輩は -> 見た
  ここで -> 始めて -> 人間という -> ものを -> 見た
  人間という -> ものを -> 見た
  ものを -> 見た
"""

import sys
from itertools import islice

from section5 import *


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    for sentence in (islice(parse_cabocha(sys.stdin), n - 1, n) if n > 0
                     else parse_cabocha(sys.stdin)):
        for chunk in sentence:
            if chunk.contains('pos', '名詞'):
                p = sentence.path_to_end(chunk)
                if p.valid():
                    print ' -> '.join(p.surfaces())

# src/048.py < data/neko.txt.cabocha > /dev/null  1.08s user 0.01s system 98% cpu 1.098 tota

# % src/048.py 6 < data/neko.txt.cabocha
# 吾輩は -> 見た
# ここで -> 始めて -> 人間という -> ものを -> 見た
# 人間という -> ものを -> 見た
# ものを -> 見た

if __name__ == '__main__':
    main()
