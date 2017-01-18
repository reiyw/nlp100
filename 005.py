#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


def n_gram(seq, n=1, mode='word', nested=False):
    if isinstance(seq, (str, unicode)) and mode == 'word':
        seq = [w for w in re.split(r' |,|\.', seq) if len(w) > 0]
    # 文字列のスライスは文字列なので，いったんリストにする
    if isinstance(seq, (str, unicode)) and mode == 'char':
        seq = list(seq)
    l = [seq[i:i + n] for i in range(len(seq))]
    if nested:
        return l
    if mode == 'word' and not nested:
        return [' '.join(v) for v in l]
    if mode == 'char' and not nested:
        return [''.join(v) for v in l]


def main():
    """05. n-gram

    与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
    この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
    """
    s = 'I am an NLPer'
    print n_gram(s, 2)
    print n_gram(s, 2, nested=True)
    print n_gram(s, 2, mode='char')
    print n_gram(s, 2, mode='char', nested=True)

if __name__ == '__main__':
    main()
