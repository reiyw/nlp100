#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
47. 機能動詞構文のマイニング

動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．46のプログラムを
以下の仕様を満たすように改変せよ．
- 「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを
  対象とする
- 述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞が
  あるときは，最左の動詞を用いる
- 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで
  辞書順に並べる
- 述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる
例えば「別段くるにも及ばんさと、主人は手紙に返事をする。」という文から，
以下の出力が得られるはずである．
  返事をする      と に は        及ばんさと 手紙に 主人は
このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて
確認せよ．
- コーパス中で頻出する述語（サ変接続名詞+を+動詞）
- コーパス中で頻出する述語と助詞パターン
"""


import sys

from section5 import *


def main():
    # MEMO: サ変接続名詞 + を に係っている場合はどうするか
    for sentence in parse_cabocha(sys.stdin):
        for chunk in sentence:
            if (not chunk.match(('pos1', 'サ変接続'), ('surface', 'を')) or
                chunk.dst is None or
                not sentence[chunk.dst].contains('pos', '動詞')):
                # 1. chunk が「サ変接続名詞 + を」の構造でない
                # 2. chunk の係り先がない
                # 3. chunk の係り先に動詞を含まない
                # 場合は対象にならない．
                continue
            # chunk: 返事を
            # verb: する
            verb = sentence[chunk.dst]
            # pred: 返事をする
            pred = '{sahen_wo}{verb}'.format(
                       sahen_wo=chunk.surface(),
                       verb=verb.find('pos', '動詞').base)
            # case_and_terms: [(と, 及ばさんと), (は, 主人は), (に, 手紙に)]
            case_and_terms = [(c.find('pos', '助詞', reverse=True).base,
                               c.surface())
                              for c in sentence.get(verb.srcs)
                              if c.contains('pos', '助詞')
                              and not c == chunk]
            case_and_terms = list(unique_everseen(case_and_terms,
                                                  key=lambda ct: ct[0]))
            if case_and_terms:
                cases, terms = zip(*sorted(case_and_terms,
                                           key=lambda ct: ct[0]))
                print '{pred}\t{cases}\t{terms}'.format(
                          pred=pred,
                          cases=' '.join(cases),
                          terms=' '.join(terms))

# src/047.py < data/neko.txt.cabocha > /dev/null  0.60s user 0.01s system 99% cpu 0.614 total

# % src/047.py < data/neko.txt.cabocha > 047.txt
#
# % head -5 047.txt
# 決心をする      と      あるこうと
# 返報をしてやる  んで    偸んで
# 昼寝をする      が      彼が
# 迫害を加える    て      追い廻して
# 投書をする      て へ   やって ほととぎすへ
#
# % cut -f 1 047.txt | sort | uniq -c | sort -rn | head -5
#      26 返事をする
#      19 挨拶をする
#      10 話をする
#       9 質問をする
#       7 真似をする
#
# % cut -f 1,2 047.txt | sort | uniq -c | sort -rn | head -5
#      10 返事をする      と
#       9 返事をする      と は
#       7 挨拶をする      で
#       5 質問をかける    と は
#       5 喧嘩をする      で

if __name__ == '__main__':
    main()
