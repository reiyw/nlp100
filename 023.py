#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""23. セクション構造

記事中に含まれるセクション名とそのレベル
（例えば"== セクション名 =="ならレベル1）を表示せよ．
"""

import sys


def main():
    for line in sys.stdin:
        if line.startswith('=='):
            print '{}: レベル {}'.format(
                line.strip('= \n'), line.count('=')/2 - 1)

# 国名: レベル 1
# 歴史: レベル 1
# 地理: レベル 1
# 気候: レベル 2
# 政治: レベル 1

if __name__ == '__main__':
    main()
