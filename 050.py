#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
50. 文区切り

(. or ; or : or ? or !) ->  空白文字 ->  英大文字というパターンを文の区切りと
見なし，入力された文書を1行1文の形式で出力せよ．
"""

import sys
import re


def main():
    for line in sys.stdin:
        for m in re.finditer(r'(.+?[.;:?!])\s+(?=[A-Z])?', line):
            print m.group(1)

# Natural language processing (NLP) is a field of computer science, artificial intelligence, and linguistics concerned with the interactions between computers and human (natural) languages.
# As such, NLP is related to the area of humani-computer interaction.
# Many challenges in NLP involve natural language understanding, that is, enabling computers to derive meaning from human or natural language input, and others involve natural language generation.
# The history of NLP generally starts in the 1950s, although work can be found from earlier periods.
# In 1950, Alan Turing published an article titled "Computing Machinery and Intelligence" which proposed what is now called the Turing test as a criterion of intelligence.

if __name__ == '__main__':
    main()
