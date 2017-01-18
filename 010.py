#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import subprocess


def main():
    """10. 行数のカウント

    行数をカウントせよ．確認にはwcコマンドを用いよ．
    """

    print sum(1 for l in sys.stdin)

    # 24
    #
    # $ wc -l hightemp.txt
    #       24 /Users/ryo-t/Projects/nlp100v2/data/hightemp.txt


if __name__ == '__main__':
    main()
