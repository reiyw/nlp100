#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
59. S式の解析

Stanford Core NLPの句構造解析の結果（S式）を読み込み，文中のすべての名詞句（NP）を
表示せよ．入れ子になっている名詞句もすべて表示すること．
"""

import sys
import re

from lxml import etree
from nltk.tree import Tree


def main():
    for parse in etree.parse(sys.stdin).iterfind('//parse'):
        tree = Tree.fromstring(parse.text)
        for subtree in tree.subtrees():
            if subtree.label() == 'NP':
                print ' '.join(subtree.leaves())
        print '*' * 20

# Natural language processing
# Wikipedia
# the free encyclopedia Natural language processing -LRB- NLP -RRB-
# the free encyclopedia Natural language processing
# NLP
# a field of computer science , artificial intelligence , and linguistics concerned with the interactions between computers and human -LRB- natural -RRB- languages
# a field of computer science
# a field
# computer science
# artificial intelligence
# linguistics concerned with the interactions between computers and human -LRB- natural -RRB- languages
# linguistics
# the interactions between computers and human -LRB- natural -RRB- languages
# the interactions
# computers and human -LRB- natural -RRB- languages
# computers
# human -LRB- natural -RRB- languages
# ********************

if __name__ == '__main__':
    main()
