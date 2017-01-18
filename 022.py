#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""22. カテゴリ名の抽出

記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
"""

import sys
import re


def main():
    # 最後に使われたパターンのコンパイル結果はキャッシュされているので
    # 正規表現を一つしか使わないのであればコンパイルの必要はない．
    #
    # ? :: 最小一致のマッチ
    reg = re.compile(r'\[\[Category:(.+?)[|\]]')
    for line in sys.stdin:
        if line.startswith('[[Category:'):  # 速い
            print reg.match(line).group(1)  # 遅い

# イギリス
# 英連邦王国
# G8加盟国
# 欧州連合加盟国
# 海洋国家
# 君主国
# 島国
# 1801年に設立された州・地域


if __name__ == '__main__':
    main()
