#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
44. 係り受け木の可視化

与えられた文の係り受け木を有向グラフとして可視化せよ．可視化には，
係り受け木をDOT言語に変換し，Graphvizを用いるとよい．また，
Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
"""

import sys
import itertools
import pydot

from p043 import Chunk


def main():
    edges = []
    for chunks in itertools.islice(Chunk.parse_cabocha(sys.stdin), 4, 5):
        for chunk in chunks:
            path = chunk.trace_chunks()
            if path:
                edges.append([chunk.join() for chunk in path])
    print edges
    g = pydot.graph_from_edges(edges, directed=True)
    g.write_png('044.png', prog='dot')

# https://dl.dropboxusercontent.com/u/80674571/nlp100/044.png

if __name__ == '__main__':
    main()
