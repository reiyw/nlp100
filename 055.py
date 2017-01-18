#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
55. 固有表現抽出

入力文中の人名をすべて抜き出せ．
"""

import sys
from itertools import groupby

from lxml import etree


def main():
    for key, group in groupby(etree.parse(sys.stdin).iterfind('//token'),
                              key=lambda t: t.findtext('NER')):
        if key == 'PERSON':
            print ' '.join(token.findtext('word') for token in group)

# Alan Turing
# Joseph Weizenbaum
# MARGIE
# Schank
# Wilensky

if __name__ == '__main__':
    main()
