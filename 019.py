#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import collections


def main():
    """19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる

    各行の１列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
    確認にはcut, uniq, sortコマンドを用いよ．
    """

    # class collections.Counter([iterable-or-mapping])
    #   要素を辞書のキーとして保存し，そのカウントを辞書の値として保存する
    #   順序付けされていないコレクション．
    #   dict のサブクラス．
    #   要素は iterable から数え上げられたり他の mapping から初期化される．
    counter = collections.Counter(
        line.split()[0].strip() for line in sys.stdin)
    # most_common([n])
    #   カウントが多いものから少ないものまで順に並べた長さ n の
    #   リストを返す． n が指定されなければすべての要素を返す．
    for word, count in counter.most_common():
        print '{} {}'.format(count, word)

    # $ cut -f 1 hightemp.txt | sort | uniq -c | sort -nr

    # 3 山形県
    # 3 埼玉県
    # 3 群馬県
    # 3 山梨県
    # 2 愛知県
    # 2 千葉県
    # 2 岐阜県
    # 2 静岡県
    # 1 高知県
    # 1 和歌山県
    # 1 大阪府
    # 1 愛媛県

if __name__ == '__main__':
    main()
