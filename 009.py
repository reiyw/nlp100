#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import random


def randrepl(matchobj):
    # Strategy:
    #   'abcde' -> ['a'], ['b', 'c', 'd'], ['e']
    #           -> ['a'], ['c', 'd', 'b'], ['e']
    #           -> ['a', 'c', 'd', 'b', 'e']
    #           -> 'abdbe'
    inner = list(matchobj.group(1))
    random.shuffle(inner)
    return ''.join(
        [matchobj.group(0)[:1]] + inner + [matchobj.group(0)[-1:]])


def main():
    """09. Typoglycemia

    スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
    それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
    ただし，長さが４以下の単語は並び替えないこととする．
    """
    s = ("I couldn't believe that I could actually understand what "
         "I was reading : the phenomenal power of the human mind .")
    s = re.sub(r"\w([\w']{3,})\w", randrepl, s)
    print s

    # I cdlou'nt bvieele that I colud alcultay undearsntd what I was readnig :
    # the pnomneahel power of the huamn mind .


if __name__ == '__main__':
    main()
