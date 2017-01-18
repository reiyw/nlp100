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
このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて
確認せよ．
- コーパス中で頻出する述語と格パターンの組み合わせ
- 「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の
  高い順）
"""


import sys

import p043


class Chunk(p043.Chunk):

    def find(self, attr, query, res='self', withobj=False):
        for morph in self.morphs:
            if getattr(morph, attr) == query:
                if not withobj:
                    return getattr(morph, res) if not res == 'self' else self
                else:
                    return (getattr(morph, res), self)
        return None

    def findall(self, attr, query, res='self', withobj=False):
        result = []
        for morph in self.morphs:
            if getattr(morph, attr) == query:
                if not withobj:
                    result.append(getattr(morph, res)
                                  if not res == 'self' else self)
                else:
                    result.append((getattr(morph, res), self))
        return result


def main():
    for chunks in Chunk.parse_cabocha(sys.stdin):
        for chunk in chunks:
            if '動詞' in chunk['pos']:
                base = chunk.find('pos', '動詞', 'base')
                particles = []
                for src in chunk.srcs_refs:
                    particles.extend(src.findall('pos', '助詞', 'base'))
                if particles:
                    print '\t'.join([base, ' '.join(sorted(particles))])

# $ ./p045.py < neko.txt.cabocha | sort -k 1,2 | uniq -c | sort -r > 045_freq.txt
# $ head -n 5 045_freq.txt
#
# $ grep する 045_freq.txt | head -3
# 442 する	を
# 174 する	に
# 127 する	と
#
# $ grep 見る 045_freq.txt | head -3
#
# $ grep 与える 045_freq.txt | head -3
#

if __name__ == '__main__':
    main()
