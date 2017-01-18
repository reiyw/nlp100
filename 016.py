#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import itertools


def main():
    """16. ファイルをN分割する

    自然数Nをコマンドライン引数などの手段で受け取り，
    入力のファイルを行単位でN分割せよ．
    同様の処理をsplitコマンドで実現せよ．
    """

    # itertools.izip_longest(*iterables[, fillvalue])
    #   各 iterable の要素をまとめるイテレータを作成する．
    #   イテレート可能オブジェクトの長さが不揃いならば，足りない値は
    #   fillvalue で埋められる．（izip() では短い方に合わせる）
    #
    # izip_longest(*([iter(s)] * n))
    #   s を長さ n のグループにまとめる常套句．
    #   1. iter(s)
    #        s 内で定義されている __iter__() を呼び出す．
    #        __iter__() は __iter__() と next() を定義した
    #        イテレータオブジェクトを返す．
    #   2. [iter(s)] * n
    #        1. の結果戻ってきたオブジェクトを n 回繰り返したリストを返す．
    #   3. *([iter(s)] * n)
    #        izip() に渡す引数のアンパック．
    #        some_func(*['foo', 'bar']) -> some_func('foo', 'bar')
    #   ファイルオブジェクトはそれ自身がイテレータであるため，
    #   1. は省略できる．
    #   例：
    #        izip_longest(*([iter('abcde')] * 2))
    #     -> izip_longest(*([<iterator ('abcde')>] * 2))
    #     -> izip_longest(*([<iterator ('abcde')>, <iterator ('abcde')>]))
    #     -> izip_longest(<iterator ('abcde')>, <iterator ('abcde')>)
    #     -> ('a', 'b') ('c', 'd') ('e', None)
    for group in itertools.izip_longest(*([sys.stdin] * int(sys.argv[1]))):
        for line in group:
            if line is not None:
                print line,
        print ''

    # 高知県  江川崎  41      2013-08-12
    # 埼玉県  熊谷    40.9    2007-08-16
    # 岐阜県  多治見  40.9    2007-08-16
    # 山形県  山形    40.8    1933-07-25
    # 山梨県  甲府    40.7    2013-08-10

    # 和歌山県        かつらぎ        40.6    1994-08-08
    # 静岡県  天竜    40.6    1994-08-04
    # 山梨県  勝沼    40.5    2013-08-10
    # 埼玉県  越谷    40.4    2007-08-16
    # 群馬県  館林    40.3    2007-08-16

    # 群馬県  上里見  40.3    1998-07-04
    # 愛知県  愛西    40.3    1994-08-05
    # 千葉県  牛久    40.2    2004-07-20
    # 静岡県  佐久間  40.2    2001-07-24
    # 愛媛県  宇和島  40.2    1927-07-22

    # 山形県  酒田    40.1    1978-08-03
    # 岐阜県  美濃    40      2007-08-16
    # 群馬県  前橋    40      2001-07-24
    # 千葉県  茂原    39.9    2013-08-11
    # 埼玉県  鳩山    39.9    1997-07-05

    # 大阪府  豊中    39.9    1994-08-08
    # 山梨県  大月    39.9    1990-07-19
    # 山形県  鶴岡    39.9    1978-08-03
    # 愛知県  名古屋  39.9    1942-08-02

    # $ split -l 5 hightemp.txt
    # xaa xab xac xad xae

if __name__ == '__main__':
    main()
