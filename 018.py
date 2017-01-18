#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import heapq
import tempfile
import itertools
import math


class RFloat(object):

    """float の大小関係を反転させたクラス"""

    def __init__(self, num):
        self.num = float(num)

    def __cmp__(self, other):
        return 1 if self.num < other.num else -1 if self.num > other.num else 0


def read_and_make_pair(f):
    """ファイルを 1 行読んで（気温，その行）なるタプルを yield する．"""
    while True:
        line = f.next()
        rf = RFloat(line.split()[2].strip())
        yield (rf, line)


def split_and_merge():
    # とりあえず 1 回のマージで終わらせる O(N^(1/2))
    n = int(math.sqrt(sum(1 for line in sys.stdin)))  # = ceil( 行数^(1/2) )
    sys.stdin.seek(0)
    tempfiles = []
    for group in itertools.izip_longest(*([sys.stdin] * n)):
        group = [elem for elem in group if elem is not None]  # None の除去
        group.sort(key=lambda k: float(k.split()[2]), reverse=True)
        tf = tempfile.TemporaryFile()
        tf.writelines(group)
        tf.seek(0)
        tempfiles.append(tf)
    # heapq.merge(*iterables)
    #   複数のソートされた入力をマージして，ソートされた値にわたる
    #   iterator を返す．ヒープの要素はタプルでもよく，その場合タプルの
    #   最初の要素同士を比較する．
    #   例:
    #     >>> list(merge([1, 5, 6], [2, 4]))
    #     [1, 2, 4, 5, 6]
    #     >>> list(merge([(3, 'foo'), (4, 'bar')], [(1, 'spam'), (2, 'egg')]))
    #     [(1, 'spam'), (2, 'egg'), (3, 'foo'), (4, 'bar')]
    for pair in heapq.merge(*[read_and_make_pair(tf) for tf in tempfiles]):
        print pair[1],


def indexing():
    # (0, 40.3) (1, 39.9) (2, 40,9) のように key と key があった文章中の
    # 位置 index のペアをソートした後，index を基に並び替える．
    # 下のやつより空間効率が良くなることが期待される．
    keys = [(i, float(line.split()[2])) for i, line in enumerate(sys.stdin)]
    keys.sort(key=lambda k: k[1], reverse=True)
    for i, key in keys:
        sys.stdin.seek(0)
        for j in range(i):
            sys.stdin.next()
        print sys.stdin.next(),


def trivial():
    lines = list(sys.stdin)
    # 引数 key で key を取り出すための関数を定義できる
    lines.sort(key=lambda s: float(s.split()[2].strip()), reverse=True)
    for line in lines:
        print line,


def main():
    """18. 各行を3コラム目の数値の降順にソート

    各行を３コラム目の数値の逆順で整列せよ
    （注意: 各行の内容は変更せずに並び替えよ）．
    確認にはsortコマンドを用いよ
    （この問題はコマンドで実行した時の結果と合わなくてもよい）．
    """
    split_and_merge()

    # $ sort -nrk 3,3 hightemp.txt

    # 高知県	江川崎	41	2013-08-12
    # 埼玉県	熊谷	40.9	2007-08-16
    # 岐阜県	多治見	40.9	2007-08-16
    # 山形県	山形	40.8	1933-07-25
    # 山梨県	甲府	40.7	2013-08-10
    # 和歌山県	かつらぎ	40.6	1994-08-08
    # 静岡県	天竜	40.6	1994-08-04
    # 山梨県	勝沼	40.5	2013-08-10
    # 埼玉県	越谷	40.4	2007-08-16
    # 群馬県	館林	40.3	2007-08-16
    # 群馬県	上里見	40.3	1998-07-04
    # 愛知県	愛西	40.3	1994-08-05
    # 千葉県	牛久	40.2	2004-07-20
    # 静岡県	佐久間	40.2	2001-07-24
    # 愛媛県	宇和島	40.2	1927-07-22
    # 山形県	酒田	40.1	1978-08-03
    # 岐阜県	美濃	40	2007-08-16
    # 群馬県	前橋	40	2001-07-24
    # 千葉県	茂原	39.9	2013-08-11
    # 埼玉県	鳩山	39.9	1997-07-05
    # 大阪府	豊中	39.9	1994-08-08
    # 山梨県	大月	39.9	1990-07-19
    # 山形県	鶴岡	39.9	1978-08-03
    # 愛知県	名古屋	39.9	1942-08-02


if __name__ == '__main__':
    main()
