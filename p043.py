#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
43. 名詞を含む文節が動詞を含む文節に係るものを抽出

名詞を含む文節が，動詞を含む文節に係るとき，
これらをタブ区切り形式で抽出せよ．
"""


import sys

import p042


class Chunk(p042.Chunk):

    def __getitem__(self, item):
        return [getattr(morph, item) for morph in self.morphs]


def main():
    for chunks in Chunk.parse_cabocha(sys.stdin):
        for chunk in chunks:
            path = chunk.trace_chunks()
            if path and '名詞' in path[0]['pos'] and '動詞' in path[1]['pos']:
                print '\t'.join(chunk.join() for chunk in path)

if __name__ == '__main__':
    main()
