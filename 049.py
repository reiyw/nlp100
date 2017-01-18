#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
49. 名詞間の係り受けパスの抽出

文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出せよ．ただし，
名詞句ペアの文節番号が$i$と$j$（$i < j$）のとき，係り受けパスは以下の仕様を
満たすものとする．

- 問題48と同様に，パスは開始文節から終了文節に至るまでの各文節の表現
  （表層形の形態素列）を"->"で連結して表現する
- 文節$i$と$j$に含まれる名詞句はそれぞれ，XとYに置換する

また，係り受けパスの形状は，以下の2通りが考えられる．

- 文節$i$から構文木の根に至る経路上に文節$j$が存在する場合: 文節$i$から文節$j$の
  パスを表示
- 上記以外で，文節$i$と文節$j$から構文木の根に至る経路上で共通の文節$k$で交わる
  場合: 文節$i$から文節$k$に至る直前のパスと文節$j$から文節$k$に至る直前までの
  パス，文節$k$の内容を"|"で連結して表示

例えば，「吾輩はここで始めて人間というものを見た。」という文
（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．

  Xは | Yで -> 始めて -> 人間という -> ものを | 見た
  Xは | Yという -> ものを | 見た
  Xは | Yを | 見た
  Xで -> 始めて -> Y
  Xで -> 始めて -> 人間という -> Y
  Xという -> Y
"""

import sys
from itertools import islice, combinations, takewhile

from section5 import *


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    for sentence in (islice(parse_cabocha(sys.stdin), n - 1, n) if n > 0
                     else parse_cabocha(sys.stdin)):
        paths_startwith_noun_phrase = [sentence.path_to_end(c) for c in sentence
                                       if c.contains('pos', '名詞')]
        for path_x, path_y in combinations(paths_startwith_noun_phrase, 2):
            # xから構文木の根に至る経路上にyが存在する場合
            if path_y[0] in path_x:
                sys.stdout.write('{} -> '.format(path_x[0].replace_np('X')))
                for chunk in takewhile(lambda c: c != path_y[0], path_x[1:]):
                    sys.stdout.write('{} -> '.format(chunk.surface()))
                print 'Y'
                continue

            # 共通の文節chunk_zで交わる場合
            for chunk_z in path_y[1:] if len(path_y) > 1 else []:
                if chunk_z in path_x:
                    sys.stdout.write('{} | {}'.format(path_x[0].replace_np('X'),
                                                      path_y[0].replace_np('Y')))
                    for chunk in takewhile(lambda c: c != chunk_z, path_y[1:]):
                        sys.stdout.write(' -> {}'.format(chunk.surface()))
                    print ' | {}'.format(chunk_z.surface())

# src/049.py < data/neko.txt.cabocha > /dev/null  2.78s user 0.01s system 99% cpu 2.796 total

# % src/049.py 6 < data/neko.txt.cabocha
# Xは | Yで -> 始めて -> 人間という -> ものを | 見た
# Xは | Yという -> ものを | 見た
# Xは | Yを | 見た
# Xで -> 始めて -> Y
# Xで -> 始めて -> 人間という -> Y
# Xという -> Y

if __name__ == '__main__':
    main()
