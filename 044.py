#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
44. 係り受け木の可視化

与えられた文の係り受け木を有向グラフとして可視化せよ．可視化には，
係り受け木をDOT言語に変換し，Graphvizを用いるとよい．また，
Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
"""

import sys
from itertools import islice

import pydot

from section5 import *


def main():
    if len(sys.argv) > 2:
        n = int(sys.argv[1])
        edges = []
        for sentence in islice(parse_cabocha(sys.stdin), n - 1, n):
            edges = [p.surfaces() for p in sentence.connect_path()]
        g = pydot.graph_from_edges(edges, directed=True)
        g.write_png(sys.argv[2], prog='dot')

# http://www.cl.ecei.tohoku.ac.jp/~ryo-t/nlp100/044.png

# %timeit !src/044.py 9 /home/ryo-t/public_html/nlp100/044.png < data/neko.txt.cabocha
# 1 loops, best of 3: 89.5 ms per loop

if __name__ == '__main__':
    main()
