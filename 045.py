#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
45. 動詞の格パターンの抽出

今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を
調査したい． 動詞を述語，動詞に係っている文節の助詞を格と考え，
述語と格をタブ区切り形式で出力せよ． ただし，出力は以下の仕様を
満たすようにせよ．

- 動詞を含む文節において，最左の動詞の基本形を述語とする
- 述語に係る助詞を格とする
- 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで
  辞書順に並べる

「吾輩はここで始めて人間というものを見た」という例文を考える． この文は
「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，
「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような
出力になるはずである．

  始める  で
  見る    は を
  見る    は を

このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて
確認せよ．

- コーパス中で頻出する述語と格パターンの組み合わせ
- 「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の
  高い順）
"""


import sys

from section5 import *


def main():
    for sentence in parse_cabocha(sys.stdin):
        for chunk in sentence:
            pred = chunk.find('pos', '動詞')
            if pred is not None:
                pred = pred.base
                cases = [c.find('pos', '助詞', reverse=True).base
                         for c in sentence.get(chunk.srcs)
                         if c.contains('pos', '助詞')]
                cases = list(unique_everseen(cases))
                if cases:
                    print '{pred}\t{cases}'.format(
                              pred=pred,
                              cases=' '.join(sorted(cases)))

# src/045.py < data/neko.txt.cabocha > /dev/null  0.95s user 0.01s system 98% cpu 0.971 total

# % src/045.py < data/neko.txt.cabocha > 045.txt
# % head -5 045.txt
# 生れる  で
# つく    か が
# 泣く    で
# する    は
# 始める  で
#
# % cat 045.txt | sort -k 1,2 | uniq -c | sort -rn -k 1 > 045_freq.txt
# % head -5 045_freq.txt
#    2136 する    は
#    1286 つく    か が
#     646 云う    は
#     533 する    が で と
#     344 思う    と
#
# % grep する 045_freq.txt | cut -f 2 | head -5
# は
# が で と
# と は は は
# から が を
# として
#
# % grep 見る 045_freq.txt | cut -f 2 | head -5
# て
# は を
# て て は
# から て
# から
#
# % grep 与える 045_freq.txt | cut -f 2 | head -5
# で に を
# に を
# て と は を
# けれども は を
# か として ば を

if __name__ == '__main__':
    main()
