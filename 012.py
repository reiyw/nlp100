#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys


def main():
    """12. 1列目をcol1.txtに，2列目をcol2.txtに保存

    各行の１列目だけを抜き出したものをcol1.txtに，
    ２列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
    確認にはcutコマンドを用いよ．
    """

    # open() の戻り値はファイルオブジェクト
    outfile1 = open('col1.txt', 'w')
    outfile2 = open('col2.txt', 'w')
    # with with_item [as target](, with_item [as target])*:
    #   1. with 文に入るとき，with_item で実装されている
    #      __enter__() メソッドが呼び出される
    #   2. target が含まれていたら __enter__() からの戻り値が代入される
    #   3. with 文から抜けるとき， with_item で実装されている
    #      __exit__() メソッドが呼び出される
    #   ファイルオブジェクトは __exit__() で close() を呼び出すので，
    #   with 文を使うことで close() を直接呼び出す必要がなくなる
    with outfile1, outfile2:
        for line in sys.stdin:
            col = line.split()
            outfile1.write(col[0] + '\n')
            outfile2.write(col[1] + '\n')

    # col1.txt	cut
    # 高知県	高知県
    # 埼玉県	埼玉県
    # 岐阜県	岐阜県
    # 山形県	山形県
    # 山梨県	山梨県
    # 和歌山県	和歌山県
    # 静岡県	静岡県
    # 山梨県	山梨県
    # 埼玉県	埼玉県
    # 群馬県	群馬県
    # 群馬県	群馬県
    # 愛知県	愛知県
    # 千葉県	千葉県
    # 静岡県	静岡県
    # 愛媛県	愛媛県
    # 山形県	山形県
    # 岐阜県	岐阜県
    # 群馬県	群馬県
    # 千葉県	千葉県
    # 埼玉県	埼玉県
    # 大阪府	大阪府
    # 山梨県	山梨県
    # 山形県	山形県
    # 愛知県	愛知県
    # col2.txt	cut
    # 江川崎	江川崎
    # 熊谷	熊谷
    # 多治見	多治見
    # 山形	山形
    # 甲府	甲府
    # かつらぎ	かつらぎ
    # 天竜	天竜
    # 勝沼	勝沼
    # 越谷	越谷
    # 館林	館林
    # 上里見	上里見
    # 愛西	愛西
    # 牛久	牛久
    # 佐久間	佐久間
    # 宇和島	宇和島
    # 酒田	酒田
    # 美濃	美濃
    # 前橋	前橋
    # 茂原	茂原
    # 鳩山	鳩山
    # 豊中	豊中
    # 大月	大月
    # 鶴岡	鶴岡
    # 名古屋	名古屋


if __name__ == '__main__':
    main()
