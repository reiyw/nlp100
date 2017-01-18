#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import itertools


def main():
    """13. col1.txtとcol2.txtをマージ

    12で作ったcol1.txtとcol2.txtを結合し，
    元のファイルの１列目と２列目をタブ区切りで並べたテキストファイルを作成せよ．
    確認にはpasteコマンドを用いよ．
    """

    infile1 = open('col1.txt')
    infile2 = open('col2.txt')
    outfile = open('col1-2.txt', 'w')
    with infile1, infile2, outfile:
        # itertools.izip(*iterables)
        #   各 iterable の要素をまとめるイテレータを作成する．
        #   zip() はリストを返すが，izip() はイテレータを返す．
        #   izip('ABCD', 'xy') --> (A, x) (B, y)
        for col1, col2 in itertools.izip(infile1, infile2):
            outfile.write(col1.replace('\n', '\t') + col2)

    # 高知県	江川崎
    # 埼玉県	熊谷
    # 岐阜県	多治見
    # 山形県	山形
    # 山梨県	甲府
    # 和歌山県	かつらぎ
    # 静岡県	天竜
    # 山梨県	勝沼
    # 埼玉県	越谷
    # 群馬県	館林
    # 群馬県	上里見
    # 愛知県	愛西
    # 千葉県	牛久
    # 静岡県	佐久間
    # 愛媛県	宇和島
    # 山形県	酒田
    # 岐阜県	美濃
    # 群馬県	前橋
    # 千葉県	茂原
    # 埼玉県	鳩山
    # 大阪府	豊中
    # 山梨県	大月
    # 山形県	鶴岡
    # 愛知県	名古屋
    #
    # $ paste col1.txt col2.txt
    # 高知県	江川崎
    # 埼玉県	熊谷
    # 岐阜県	多治見
    # 山形県	山形
    # 山梨県	甲府
    # 和歌山県	かつらぎ
    # 静岡県	天竜
    # 山梨県	勝沼
    # 埼玉県	越谷
    # 群馬県	館林
    # 群馬県	上里見
    # 愛知県	愛西
    # 千葉県	牛久
    # 静岡県	佐久間
    # 愛媛県	宇和島
    # 山形県	酒田
    # 岐阜県	美濃
    # 群馬県	前橋
    # 千葉県	茂原
    # 埼玉県	鳩山
    # 大阪府	豊中
    # 山梨県	大月
    # 山形県	鶴岡
    # 愛知県	名古屋


if __name__ == '__main__':
    main()
