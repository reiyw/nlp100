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
from itertools import islice

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


class Chunks(list):

    def __init__(self, *chunks):
        list.__init__(self, *chunks)

    def __str__(self):
        s1 = '-' * 40
        s2 = '\n'.join(chunk.__str__() for chunk in self)
        return '{}\n{}'.format(s1, s2)


class Sentence(Chunks):

    def __init__(self, chunk2morphs):
        super(Sentence, self).__init__(Chunk(chunk, morphs) for chunk, morphs
                                       in chunk2morphs)

        # 係り先 Chunk の srcs に係り元の slf を追加
        for chunk in self:
            if chunk.dst is not None:
                self[chunk.dst].srcs.append(chunk.slf)


def parse_cabocha(cabocha_seq):
    """CaboCha の係り受け解析結果をパースする．

    Yields:
        Sentence オブジェクト
    """
    for startswith_eos, sentence in groupby(cabocha_seq,
                                            key=lambda l: l == 'EOS\n'):
        if not startswith_eos:
            # [chunk1, [morph11, morph12], chunk2, [morph21], ...]
            stripe = [next(g) if k == Line.CHUNK else list(g) for k, g in
                      groupby(sentence, key=classify_cabocha_line)]
            # [[chunk1, [morph11, morph12]], [chunk2, [morph21]], [...], ...]
            yield Sentence(zip(*[iter(stripe)]*2))


def main():
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        for sentence in islice(parse_cabocha(sys.stdin), n - 1, n):
            print sentence
    else:
        for sentence in parse_cabocha(sys.stdin):
            print sentence

# ----------------------------------------
# * 文節 0: 係り先 9, 係り元 []
# しかし  しかし  接続詞  *
# * 文節 1: 係り先 2, 係り元 []
# その    その    連体詞  *
# * 文節 2: 係り先 5, 係り元 [1]
# 当時    当時    名詞    副詞可能
# は      は      助詞    係助詞
# * 文節 3: 係り先 4, 係り元 []
# 何      何      名詞    代名詞
# という  という  助詞    格助詞
# * 文節 4: 係り先 5, 係り元 [3]
# 考      考      名詞    一般
# も      も      助詞    係助詞
# * 文節 5: 係り先 9, 係り元 [2, 4]
# なかっ  ない    形容詞  自立
# た      た      助動詞  *
# から    から    助詞    接続助詞
# * 文節 6: 係り先 7, 係り元 []
# 別段    別段    副詞    一般
# * 文節 7: 係り先 9, 係り元 [6]
# 恐し    恐い    形容詞  自立
# * 文節 8: 係り先 9, 係り元 []
# いとも  いとも  副詞    一般
# * 文節 9: 係り先 None, 係り元 [0, 5, 7, 8]
# 思わ    思う    動詞    自立
# なかっ  ない    助動詞  *
# た      た      助動詞  *
# 。      。      記号    句点

# %timeit !src/041.py 9 < data/neko.txt.cabocha
# 100 loops, best of 3: 17 ms per loop

if __name__ == '__main__':
    main()
