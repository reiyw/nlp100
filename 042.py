#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
42. 係り元と係り先の文節の表示

係り元の文節と係り先の文節の表現をタブ区切り形式ですべて抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．
"""

import sys

from section5 import *

# Chunk に追加
#
# def valid(self):
#     "記号だけからなる文節でなければ valid"
#     return any(m.pos != '記号' for m in self.morphs)
#
# def surface(self):
#     return ''.join(m.surface for m in self.morphs if m.pos != '記号')

# Chunks に追加
#
# def valid(self):
#     "valid な文節数が 1 より大きいなら true を返す．"
#     return sum(chunk.valid() for chunk in self) > 1
#
# def surfaces(self):
#     return [chunk.surface() for chunk in self]

# Sentence に追加
#
# def connect_path(self):
#     "一文について [Path(係り元，係り先), ...] を返す"
#     res = [Path([c, self[c.dst]]) for c in self if c.dst is not None]
#     return [p for p in res if p.valid()]


class Path(Chunks):

    def __init__(self, *chunks):
        super(Path, self).__init__(*chunks)


def main():
    for sentence in parse_cabocha(sys.stdin):
        for path in sentence.connect_path():
            print '\t'.join(path.surfaces())

# 吾輩は  猫である
# 名前は  無い
# まだ    無い
# どこで  生れたか
# 生れたか        つかぬ

# %timeit !src/042.py < data/neko.txt.cabocha
# 1 loops, best of 3: 1.41 s per loop

if __name__ == '__main__':
    main()
