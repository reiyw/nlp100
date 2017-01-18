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

import p045


class Chunk(p045.Chunk):

    def extract_case_frame(self):
        srcs = []
        for src in self.srcs_refs:
            srcs.extend(
                src.findall('pos', '助詞', 'base', withobj=True))
        if srcs:
            particles, terms = zip(*sorted(srcs, key=lambda s: s[0]))
            terms = [chunk.join() for chunk in terms]
            return '\t'.join((' '.join(particles), ' '.join(terms)))
        return False


def main():
    for chunks in Chunk.parse_cabocha(sys.stdin):
        for chunk in chunks:
            if '動詞' in chunk['pos']:
                predicate = chunk.find('pos', '動詞', 'base')
                case_frame = chunk.extract_case_frame()
                if case_frame:
                    print '{}\t{}'.format(predicate, case_frame)

# $ ./p046.py < neko.txt.cabocha > 046.txt
# $ head -n 10 046.txt
# 生れる	で	どこで
# つく	か が	生れたか 見当が
# 泣く	で	所で
# する	だけ て は	いた事だけは 泣いて いた事だけは
# 始める	で	ここで

if __name__ == '__main__':
    main()
