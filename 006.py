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
    """06. 集合

    "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ,
    XとYとして求め，XとYの和集合，積集合，補集合を求めよ．
    さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
    """
    X = frozenset(n_gram('paraparaparadise', 2, mode='char'))
    Y = frozenset(n_gram('paragraph', 2, mode='char'))
    print X.union(Y)
    print X.intersection(Y)
    print X.difference(Y)  # X における Y の補集合
    print Y.difference(X)  # Y における X の補集合
    print "'se' is{}in X.".format(' ' if 'se' in X else ' not ')
    print "'se' is{}in Y.".format(' ' if 'se' in Y else ' not ')

if __name__ == '__main__':
    main()
