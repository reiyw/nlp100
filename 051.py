#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
51. 単語の切り出し

空白を単語の区切りとみなし，50の出力を入力として受け取り，1行1単語の形式で出力せよ．
ただし，文の終端では空行を出力せよ．
"""

import sys


def main():
    for line in sys.stdin:
        for word in line.split(' '):
            print word

# human
# (natural)
# languages.
#
# As
# such,
# NLP

if __name__ == '__main__':
    main()
