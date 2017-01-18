#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
40. 係り受け解析結果の読み込み（形態素）

形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），
基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に
持つこととする．さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，
各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．
"""

import sys
from itertools import groupby


class Morph(object):

    def __init__(self, line):
        self.surface, remain = line.strip().split('\t')
        self.pos, self.pos1, _, _, _, _, self.base = remain.split(',')[:7]

    def __str__(self):
        return '{surface}\t{base}\t{pos}\t{pos1}'.format(**self.__dict__)

    def __getitem__(self, item):
        # attr = 'surface'; morph[attr] で読み出せるようになる．
        # これをしないと getattr() とか使う必要があってちょっと面倒．
        return self.__dict__[item]


class Line(object):
    EOS, CHUNK, MORPH = range(3)


def classify_cabocha_line(line):
    if line.startswith('EOS'):
        return Line.EOS
    elif line.startswith('* '):
        return Line.CHUNK
    else:
        return Line.MORPH


def parse_cabocha(cabocha_seq):
    for startswith_eos, sentence in groupby(cabocha_seq,
                                            key=lambda l: l.startswith('EOS')):
        if not startswith_eos:
            for key, group in groupby(sorted(sentence, key=classify_cabocha_line),
                                      key=classify_cabocha_line):
                if key == Line.MORPH:
                    yield [Morph(line) for line in group]


def main():
    for morphs in parse_cabocha(sys.stdin):
        for morph in morphs:
            print morph


if __name__ == '__main__':
    main()
