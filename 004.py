#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


def main():
    """04. 元素記号

    "Hi He Lied Because Boron Could Not Oxidize Fluorine.
    New Nations Might Also Sign Peace Security Clause.
    Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の
    単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，
    取り出した文字列から単語の位置（先頭から何番目の単語か）への
    連想配列（辞書型）を作成せよ．
    """
    s = ("Hi He Lied Because Boron Could Not Oxidize Fluorine. "
         "New Nations Might Also Sign Peace Security Clause. "
         "Arthur King Can.")
    one_chars = (1, 5, 6, 7, 8, 9, 15, 16, 19)
    words = tuple(w for w in re.split(r' |,|\.', s) if len(w) > 0)
    element_dict = {}
    for i, w in enumerate(words, start=1):
        if i in one_chars:
            element_dict[w[:1]] = i
        else:
            element_dict[w[:2]] = i
    print element_dict


if __name__ == '__main__':
    main()
