#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


def cipher(s):
    # re.sub(pattern, repl, string[, count, flags])
    #   string 内の pattern を repl で置換する．
    #   repl は関数でもよい．この関数は 1 つの MatchObject を引数にとり，
    #   置換文字列を返す．matchobj.group(0) でマッチ全体を参照できる．
    #
    # ord(c)
    #   c が unicode 文字列の場合，Unicode コードポイントを表す整数を返す．
    #   c が 8 ビット文字列の場合，そのバイトの値を返す．
    #   日本語を使わなければ単に ASCII コードを返すものと考えて差し支えない．
    #
    # chr(i)
    #   ASCII コードが i となるような文字を返す．ord() の逆．
    return re.sub(r'[a-z]', lambda m: chr(219 - ord(m.group(0))), s)


def main():
    """08. 暗号文

    与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
    - 英小文字ならば(219 - 文字コード)の文字に置換
    - その他の文字はそのまま出力
    この関数を用い，英語のメッセージを暗号化・復号化せよ．
    """

    s = 'This is a test.'
    print s
    print cipher(s)
    print cipher(cipher(s))

    # This is a test.
    # Tsrh rh z gvhg.
    # This is a test.


if __name__ == '__main__':
    main()
