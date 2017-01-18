#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""37. 頻度上位10語

出現頻度が高い10語とその出現頻度をグラフで表示せよ．
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
    words, counts = zip(*c.most_common(10))
    words_pos = np.arange(len(words))

    fig, ax = plt.subplots()
    ax.bar(words_pos, counts, .8)
    ax.set_title(u'出現頻度上位 10 語')
    ax.set_xlabel(u'単語')
    ax.set_ylabel(u'出現頻度')
    ax.set_xticks(words_pos + .4)
    ax.set_xticklabels([unicode(w, encoding='utf-8') for w in words])

    if len(sys.argv) > 1:
        plt.savefig(sys.argv[1])
    else:
        plt.show()

# http://www.cl.ecei.tohoku.ac.jp/~ryo-t/graphs/037.png

if __name__ == '__main__':
    main()
