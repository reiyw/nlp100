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

import p046


class Chunk(p046.Chunk):

    def getitems(self, *attrs):
        if len(attrs) == 1:
            return [morph[attrs[0]] for morph in self.morphs]
        else:
            result = []
            for morph, attr in zip(self.morphs, attrs):
                result.append(morph[attr])
            return result


def main():
    for chunks in Chunk.parse_cabocha(sys.stdin):
        for chunk in chunks:
            if (chunk.getitems('pos1', 'surface') == ['サ変接続', 'を']
                and '動詞' in chunk.dst_ref.getitems('pos')):
                predicate = (chunk.join()
                             + chunk.dst_ref.find('pos', '動詞', 'base'))
                case_frame = chunk.extract_case_frame()
                if case_frame:
                    print '{}\t{}'.format(predicate, case_frame)


# $ ./p047.py < neko.txt.cabocha > 047.txt
# $ cut -f 1,1 047.txt | sort | uniq -c | sort -r | head -n 10
# 14 返事をする
# 13 挨拶をする
#  9 真似をする
#  6 話を聞く
#  5 質問をかける
#  5 話をする
#  3 質問をする
#  3 議論をする
#  3 談話を聞く
#  3 経験をする

# $ grep "\t[^\t]\+\t" 047.txt | cut -d : -f 2- | cut -f 1,2 | sort | uniq -c | sort -r | head -n 10"]"
# 4 真似をする の
# 3 挨拶をする の
# 3 話を聞く   の
# 3 話をする   の
# 2 観察を怠る の
# 2 注意を惹く の
# 2 平均を破る の
# 2 修行をする の
# 1 ストライキをしでかす       や
# 1 連想をかたちづくる の

if __name__ == '__main__':
    main()
