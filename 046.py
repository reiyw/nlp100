#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
46. 動詞の格フレーム情報の抽出

45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節
そのもの）をタブ区切り形式で出力せよ．45の仕様に加えて，以下の仕様を
満たすようにせよ．
- 項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
- 述語に係る文節が複数あるときは，助詞と同一の基準でスペース区切りで並べる
「吾輩はここで始めて人間というものを見た」という例文を考える． この文は
「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，
「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような
出力になるはずである．
  始める  で      ここで
  見る    は を   吾輩は ものを
"""

import sys

from section5 import *


def main():
    for sentence in parse_cabocha(sys.stdin):
        for chunk in sentence:
            if chunk.contains('pos', '動詞'):
                pred = chunk.find('pos', '動詞').base
                # [(は, 吾輩は), (を, ものを)]
                case_and_terms = [(c.find('pos', '助詞', reverse=True).base,
                                   c.surface())
                                  for c in sentence.get(chunk.srcs)
                                  if c.contains('pos', '助詞')]
                case_and_terms = list(unique_everseen(case_and_terms,
                                                      key=lambda ct: ct[0]))
                if case_and_terms:
                    cases, terms = zip(*sorted(case_and_terms,
                                               key=lambda ct: ct[0]))
                    print '{pred}\t{cases}\t{terms}'.format(
                              pred=pred,
                              cases=' '.join(cases),
                              terms=' '.join(terms))

# src/046.py < data/neko.txt.cabocha > /dev/null  1.04s user 0.01s system 99% cpu 1.048 total

# % src/046.py < data/neko.txt.cabocha | head -5
# 生れる  で      どこで
# つく    か が   生れたか 見当が
# 泣く    で      所で
# する    は      事だけは
# 始める  で      ここで

if __name__ == '__main__':
    main()
