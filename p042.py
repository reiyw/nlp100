#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
42. 係り元と係り先の文節の表示

係り元の文節と係り先の文節の表現をタブ区切り形式ですべて抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．
"""

import sys

from section5 import *


    def join(self):
        "表層形を連結した文字列を返す．ただし，記号は除く．"
        surfaces = []
        for morph in self.morphs:
            if not morph.pos == '記号':
                surfaces.append(morph.surface)
        return ''.join(surfaces)

    def __is_composed_of_symbols(self):
        '記号だけからなる文節であるかを調べる．'
        return (True if all(morph.pos == '記号' for morph in self.morphs)
                else False)

    def trace_chunks(self, min_depth=2, max_depth=2):
        """係り先の Chunk を順々に辿り，途中の Chunk への参照のリストを返す．
        返されるリストの長さ l は min_depth <= l <= max_depth を満たす．

        """
        chunks = []
        chunk = self
        while chunk is not None and len(chunks) < max_depth:
            if not chunk.__is_composed_of_symbols():
                chunks.append(chunk)
            chunk = chunk.dst_ref
        return chunks if min_depth <= len(chunks) else []


class Chunks(list):

    def __call__(self, *more):
        list.__call__(*more)

    def getattributes(self, attr, cond):
        result = []
        for chunk in self:
            for morph in chunk.morphs:
                result.append(morph[attr] if morph[cond[0]] == cond[1] else '')
        return result


class Path(list):

    def __init__(self, *args):
        list.__init__(self, *args)

    def


def main():
    for chunks in parse_cabocha(sys.stdin):
        for chunk in chunks:
            path = chunk.trace_chunks(2, 2)
            if path:
                Chunks([chunk]).print_attr('surface')
                print '\t'.join(chunk.join() for chunk in path)


if __name__ == '__main__':
    main()
