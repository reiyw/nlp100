#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""34. 「AのB」

２つの名詞が「の」で連結されている名詞句を抽出せよ．
"""

import sys
import collections

import p030


def main():
    # マップ型を値に持つ deque
    sliding_window = collections.deque([{}] * 3, 3)

    for sentence in p030.parse_mecab_seq(sys.stdin):
        for morph in sentence:
            sliding_window.append(morph)
            if (sliding_window[0].get('pos') == '名詞' and
                sliding_window[1].get('pos1') == '連体化' and
                sliding_window[2].get('pos') == '名詞'):
                # 真ん中が連体化であることをチェックすれば良さそうだけど一応
                print ''.join(m['surface'] for m in sliding_window)
        # 文末または文頭に連体化が来た時に誤って抽出してしまう可能性を排除
        sliding_window.append({})

# 彼の掌
# 掌の上
# 書生の顔
# はずの顔
# 顔の真中

if __name__ == '__main__':
    main()
