#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import itertools


def main():
    """14. 先頭からN行を出力

    自然数Nをコマンドライン引数などの手段で受け取り，
    入力のうち先頭のN行だけを表示せよ．
    確認にはheadコマンドを用いよ．
    """

    # itertools.islice(iterable[, start], stop[, step])
    #   iterable から要素を選択して返すイテレータを作成する．
    for line in itertools.islice(sys.stdin, int(sys.argv[1])):
        print line,

    # 高知県	江川崎	41	2013-08-12
    # 埼玉県	熊谷	40.9	2007-08-16
    # 岐阜県	多治見	40.9	2007-08-16
    # 山形県	山形	40.8	1933-07-25
    # 山梨県	甲府	40.7	2013-08-10
    #
    # $ head -n 5 hightemp.txt
    # 高知県	江川崎	41	2013-08-12
    # 埼玉県	熊谷	40.9	2007-08-16
    # 岐阜県	多治見	40.9	2007-08-16
    # 山形県	山形	40.8	1933-07-25
    # 山梨県	甲府	40.7	2013-08-10


if __name__ == '__main__':
    main()
