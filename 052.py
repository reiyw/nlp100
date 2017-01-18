#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
52. ステミング

51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，単語と
語幹をタブ区切り形式で出力せよ． Porterのステミングアルゴリズムの実装として，
stemmingモジュールを利用するとよい．
"""

import sys

from stemming import porter


def main():
    for word in sys.stdin:
        word = word.strip()
        print '{}\t{}'.format(word, porter.stem(word))

# Natural	Natur
# language	languag
# processing	process
# (NLP)	(NLP)
# is	is

if __name__ == '__main__':
    main()
