#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
53. Tokenization

Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．また，この
XMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．
"""

import sys
import xml.parsers.expat

from lxml import etree


class Handler(object):

    def __init__(self):
        self.is_word = False

    def start_element_handler(self, name, _):
        if name == 'word':
            self.is_word = True

    def end_element_handler(self, _):
        self.is_word = False

    def character_date_handler(self, data):
        if self.is_word:
            print data


def parse_with_expat(infile):
    p = xml.parsers.expat.ParserCreate()
    h = Handler()
    p.StartElementHandler = h.start_element_handler
    p.EndElementHandler = h.end_element_handler
    p.CharacterDataHandler = h.character_date_handler
    p.ParseFile(infile)


def one_liner(infile):
    [sys.stdout.write(elem.text + '\n') for elem in etree.parse(infile).iterfind('//word')]


def main():
    # 明示的にすべて書くことで coreference の方まで辿らなくなるので *少し* 早い．
    for word in etree.parse(sys.stdin).xpath(
                    '/root/document/sentences/sentence/tokens/token/word'):
        print word.text

    # find(), iterfind() では root の次から書き始める
    # for word in etree.parse(sys.stdin).iterfind('document/sentences/sentence/tokens/token/word'):
    #     print word.text

    # context = etree.iterparse(sys.stdin, tag='word')
    # for _, elem in context:
    #     print elem.text

# java -cp "*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref -file nlp.txt

# Natural
# language
# processing
# From
# Wikipedia

if __name__ == '__main__':
    main()
