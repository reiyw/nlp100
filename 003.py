#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


def main():
    """03. 円周率

    "Now I need a drink, alcoholic of course, after the heavy lectures
    involving quantum mechanics."という文を単語に分解し，
    各単語の（アルファベットの）文字数を先頭から順に並べたリストを作成せよ．
    """

    s = ("Now I need a drink, alcoholic of course, after the heavy "
         "lectures involving quantum mechanics.")
    print [len(w) for w in re.split(r' |,|\.', s) if len(w) > 0]


if __name__ == '__main__':
    main()
