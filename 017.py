#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def main():
    """17. １列目の文字列の異なり

    １列目の文字列の種類（異なる文字列の集合）を求めよ．
    確認にはsort, uniqコマンドを用いよ．
    """

    uniq = set()
    for line in sys.stdin:
        uniq.add(line.split()[0].strip())
    for s in uniq:
        print s

    # $ cut -f 1 hightemp.txt | sort | uniq

    # 愛知県
    # 山形県
    # 岐阜県
    # 千葉県
    # 埼玉県
    # 高知県
    # 群馬県
    # 山梨県
    # 和歌山県
    # 愛媛県
    # 大阪府
    # 静岡県

if __name__ == '__main__':
    main()
