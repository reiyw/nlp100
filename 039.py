#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""39. Zipfの法則

単語の出現頻度順位を横軸，その出現頻度を縦軸として，
両対数グラフをプロットせよ．
"""

import sys
from collections import Counter
from itertools import chain

import numpy as np
import matplotlib.pyplot as plt

import p030


def main():
    c = Counter(morph['base'] for morph in
                chain.from_iterable(p030.parse_mecab_seq(sys.stdin)))
    words, count = zip(*c.most_common())
    x = np.arange(1, len(words) + 1)

    plt.loglog(x, count)
    plt.title(u'Zipf の法則')
    plt.xlabel(u'出現頻度順位')
    plt.ylabel(u'出現頻度')

    if len(sys.argv) > 1:
        plt.savefig(sys.argv[1])
    else:
        plt.show()

# http://www.cl.ecei.tohoku.ac.jp/~ryo-t/graphs/039.png

if __name__ == '__main__':
    main()
