#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
54. 品詞タグ付け

Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で
出力せよ．
"""

import sys

from lxml import etree


def one_liner(infile):
    [sys.stdout.write('\t'.join(elem.text for elem in token.iter('word', 'lemma', 'POS')) + '\n') for token in etree.parse(infile).iterfind('//token')]


def main():
    for token in etree.parse(sys.stdin).iterfind('//token'):
        print '\t'.join(elem.text for elem in token.iter('word', 'lemma', 'POS'))

    # context = etree.iterparse(sys.stdin, tag='token')
    # for _, token in context:
    #     print '\t'.join(elem.text for elem in token.iter('word', 'lemma', 'POS'))

# Natural natural JJ
# language        language        NN
# processing      processing      NN
# From    from    IN
# Wikipedia       Wikipedia       NNP

if __name__ == '__main__':
    main()
