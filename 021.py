#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""21. カテゴリ名を含む行を抽出

記事中でカテゴリ名を宣言している行を抽出せよ．
"""

import sys


def main():
    for line in sys.stdin:
        if line.startswith('[[Category:'):
            print line,

# [[Category:イギリス|*]]
# [[Category:英連邦王国|*]]
# [[Category:G8加盟国]]
# [[Category:欧州連合加盟国]]
# [[Category:海洋国家]]
# [[Category:君主国]]
# [[Category:島国|くれいとふりてん]]
# [[Category:1801年に設立された州・地域]]


if __name__ == '__main__':
    main()
