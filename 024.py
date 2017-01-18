#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""24. ファイル参照の抽出

記事から参照されているメディアファイルをすべて抜き出せ．
"""

import sys
import re


def main():
    for line in sys.stdin:
        for m in re.finditer(r'([fF]ile:|ファイル:)(.+?)\|', line):
            print m.group(2)

# Royal Coat of Arms of the United Kingdom.svg
# Battle of Waterloo 1815.PNG
# The British Empire.png
# Uk topo en.jpg
# BenNevis2005.jpg

if __name__ == '__main__':
    main()
