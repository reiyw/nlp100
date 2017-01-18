#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
57. 係り受け解析

Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）を有向グラフとして
可視化せよ．可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．また，
Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
"""

import sys

from lxml import etree
import pydot


def main():
    n = int(sys.argv[1])
    graph = pydot.Dot(graph_type='digraph')
    tree = etree.parse(sys.stdin)
    for dep in tree.find('//sentence[@id="{}"]/dependencies'
                         '[@type="collapsed-dependencies"]'.format(n)):
        governor, dependent = dep.iter('governor', 'dependent')

        graph.add_node(pydot.Node(governor.get('idx'), label=governor.text))
        graph.add_node(pydot.Node(dependent.get('idx'), label=dependent.text))

        graph.add_edge(pydot.Edge(governor.get('idx'), dependent.get('idx'),
                                  label=dep.get('type')))

    graph.write_png(sys.argv[2], prog='dot')

# http://www.cl.ecei.tohoku.ac.jp/~ryo-t/nlp100/057.png

if __name__ == '__main__':
    main()
