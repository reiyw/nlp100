#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
56. 共参照解析

Stanford Core NLPの共参照解析の結果に基づき，文中の参照表現（mention）を
代表参照表現（representative mention）に置換せよ．ただし，置換するときは，
「代表参照表現（参照表現）」のように，元の参照表現が分かるように配慮せよ．
"""

import sys

from lxml import etree


def main():
    tree = etree.parse(sys.stdin)
    mentions = {}

    for coref in tree.xpath('/root/document/coreference/coreference'):
        r_mention = coref.findtext('mention[@representative]/text')
        for mention in coref.xpath('mention[not(@representative)]'):
            sentence, start, end, mention = mention.iter('sentence', 'start',
                                                         'end', 'text')
            mentions.update({sentence.text: {start.text:
                            (end.text, mention.text, r_mention)}})

    for sentence in tree.xpath('/root/document/sentences/sentence'):
        s_id = sentence.get('id')
        if s_id in mentions:
            it = sentence.iterfind('tokens/token')  # 後で再利用したいから
            for token in it:
                t_id = token.get('id')
                if t_id in mentions[s_id]:
                    # 代表参照表現（参照表現）
                    sys.stdout.write('{} ({}) '.format(
                        mentions[s_id][t_id][2],
                        mentions[s_id][t_id][1]))
                    # 適当な位置まで読み進めて出力
                    for token in it:
                        if token.get('id') == mentions[s_id][t_id][0]:
                            sys.stdout.write(token.findtext('word') + ' ')
                            break
                else:
                    sys.stdout.write(token.findtext('word') + ' ')
            print ''

# Natural language processing From Wikipedia , the free encyclopedia Natural language processing -LRB- NLP -RRB- is the free encyclopedia Natural language processing -LRB- NLP -RRB- (a field of computer science) , artificial intelligence , and linguistics concerned with the interactions between computers and human -LRB- natural -RRB- languages .
# Many challenges in NLP involve natural language understanding , that is , enabling computers (computers) to derive meaning from human or natural language input , and others involve natural language generation .
# In 1950 , Alan Turing published an article titled `` Computing Machinery and Intelligence '' which proposed what is now called the Alan Turing (Turing) test as a criterion of intelligence .
# The authors claimed that within three or five years , a solved problem (machine translation) would be a solved problem .
# Little further research in a solved problem (machine translation) was conducted until the late 1980s , when the first statistical machine translation systems were developed .

if __name__ == '__main__':
    main()
