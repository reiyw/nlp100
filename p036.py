#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""36. 単語の出現頻度

文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
"""

import sys
from collections import Counter
from itertools import chain

import p030


def main():
    c = Counter(morph['base'] for morph in
                chain.from_iterable(p030.parse_mecab_seq(sys.stdin)))
    for word, count in c.most_common():
        print word, count

# の 9196
# 。 7486
# て 6799
# 、 6772
# は 6416

if __name__ == '__main__':
    main()
