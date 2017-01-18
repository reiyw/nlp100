#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import collections


def main():
    """15. 末尾のN行を出力

    自然数Nをコマンドライン引数などの手段で受け取り，
    入力のうち末尾のN行だけを表示せよ．
    確認にはtailコマンドを用いよ．
    """

    # collections.deque(iterable[, maxlen]])
    #   iterable で与えられるデータから，新しい deque オブジェクトを
    #   左から右に初期化して返す．
    #   Deque はどちらの側からも append と pop が可能で、
    #   スレッドセーフでメモリ効率がよく，どちらの方向からもおよそ
    #   O(1) のパフォーマンスで実行できる．
    lines = collections.deque(sys.stdin, int(sys.argv[1]))
    while lines:
        print lines.popleft(),

    # 埼玉県	鳩山	39.9	1997-07-05
    # 大阪府	豊中	39.9	1994-08-08
    # 山梨県	大月	39.9	1990-07-19
    # 山形県	鶴岡	39.9	1978-08-03
    # 愛知県	名古屋	39.9	1942-08-02
    #
    # $ tail -n 5 hightemp.txt
    # 埼玉県	鳩山	39.9	1997-07-05
    # 大阪府	豊中	39.9	1994-08-08
    # 山梨県	大月	39.9	1990-07-19
    # 山形県	鶴岡	39.9	1978-08-03
    # 愛知県	名古屋	39.9	1942-08-02


if __name__ == '__main__':
    main()
