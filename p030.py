#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""30. 形態素解析結果の読み込み

形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は表層形（surface），基本形（base），品詞（pos），
品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素
（マッピング型）のリストとして表現せよ．
"""

import sys
from itertools import groupby


def parse_mecab_seq(mecab_seq):
    """MeCab で形態素解析されたデータをパースする．

    Yields:
        surface, base, pos, pos1 をキーとする辞書型のリスト（1 文）
    """
    def parse_morph_line(line):
        surface, remain = line.strip().split('\t')
        pos, pos1, _, _, _, _, base = remain.split(',')[:7]
        return {'surface': surface, 'base': base, 'pos': pos, 'pos1': pos1}

    for key, group in groupby(mecab_seq, key=lambda l: l.startswith('EOS')):
        if not key:  # EOS で始まらないグループ
            yield [parse_morph_line(line) for line in group]


def pprint(sentence):
    """形態素のリスト（1 文）を綺麗に出力する．"""
    print '*' * 40
    print '表層形\t基本形\t品詞\t品詞細分類1'
    print '-' * 40
    for morph in sentence:
        print '{0[surface]}\t{0[base]}\t{0[pos]}\t{0[pos1]}'.format(morph)


def main():
    [pprint(sentence) for sentence in parse_mecab_seq(sys.stdin)]

# ****************************************
# 表層形	基本形	品詞	品詞細分類1
# ----------------------------------------
# 　	　	記号	空白
# 吾輩	吾輩	名詞	代名詞
# は	は	助詞	係助詞
# 猫	猫	名詞	一般
# で	だ	助動詞	*
# ある	ある	助動詞	*
# 。	。	記号	句点

if __name__ == '__main__':
    main()
