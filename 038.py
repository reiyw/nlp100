#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""38. ヒストグラム

単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の
種類数を棒グラフで表したもの）を描け．
"""


import sys
from collections import Counter
from itertools import chain

import matplotlib.pyplot as plt

import p030


def main():
    c = Counter(morph['base'] for morph in
                chain.from_iterable(p030.parse_mecab_seq(sys.stdin)))
    words, count = zip(*c.most_common())

    plt.hist(count, bins=50, log=True)
    plt.title(u'単語の出現頻度のヒストグラム')
    plt.xlabel(u'出現頻度')
    plt.ylabel(u'出現頻度をとる単語の種類数')

    if len(sys.argv) > 1:
        plt.savefig(sys.argv[1])
    else:
        plt.show()

# http://www.cl.ecei.tohoku.ac.jp/~ryo-t/graphs/038.png

if __name__ == '__main__':
    main()
