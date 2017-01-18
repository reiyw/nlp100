#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
41. 係り受け解析結果の読み込み（文節・係り受け）

文節を表すクラスChunkを実装せよ．このクラスは形態素（Morphオブジェクト）の
リスト（morphs），係り先文節インデックス番号（dst），
係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
さらに，入力テキストのCaboChaの解析結果を読み込み，１文を
Chunkオブジェクトのリストとして表現し，8文目の文節の文字列と係り先を
表示せよ．
"""

import sys
from itertools import groupby

from section5 import *


class Chunk(object):

    def __init__(self, chunk, morphs):
        # * {文節番号} {係り先}D x/x x
        ast, slf_str, dst_plus_D = chunk.split(' ')[:3]
        dst_str = dst_plus_D[:-1]

        self.slf = int(slf_str)
        self.dst = None if dst_str == '-1' else int(dst_str)
        self.morphs = [Morph(line) for line in morphs]
        self.srcs = []

    def __str__(self):
        s1 = '* 文節 {slf}: 係り先 {dst}, 係り元 {srcs}'.format(**self.__dict__)
        s2 = '\n'.join(morph.__str__() for morph in self.morphs)
        return '{}\n{}'.format(s1, s2)


class Sentence(object):

    def __init__(self, chunks, morphs_lists):
        "Sentence([chunk1, chunk2, ...], [[morph11, morph12,], [morph21], ...])"
        self.chunks = [Chunk(chunk, morphs) for chunk, morphs in
                       zip(chunks, morphs_lists)]

        # 係り先 Chunk の srcs に係り元の slf を追加
        for chunk in self.chunks:
            if chunk.dst is not None:
                self.chunks[chunk.dst].srcs.append(chunk.slf)

    def __str__(self):
        s1 = '=' * 40
        s2 = '\n'.join(chunk.__str__() for chunk in self.chunks)
        return '{}\n{}'.format(s1, s2)


def parse_cabocha(cabocha_seq):
    """CaboCha で係り受け解析されたデータをパースする．

    Yields:
        Chunk オブジェクトのリスト（1 文）
    """
    for startswith_eos, sentence in groupby(cabocha_seq,
                                            key=lambda l: l.startswith('EOS')):
        if not startswith_eos:
            classified = [next(g) if k == Line.CHUNK else list(g) for k, g in
                          groupby(sentence, key=classify_cabocha_line)]
            yield Sentence(classified[0::2], classified[1::2])


def main():
    for sentence in parse_cabocha(sys.stdin):
        print sentence


if __name__ == '__main__':
    main()
