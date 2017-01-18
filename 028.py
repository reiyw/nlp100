#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""28. MediaWikiマークアップの除去

27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り
除去し，国の基本情報を整形せよ．
"""

import sys
import re
from functools import partial
import json


def main():
    # functools.partial(func[, *args][, **keywords])
    #   関数の引数の一部を凍結する．
    #   p = partial(re.sub, pattern, repl) とすると
    #   re.sub(pattern, repl, string) と p(string) が等価になる．
    partialsubs = (
        # <ref 以降削除
        partial(re.sub, re.compile(r'<ref.+'), ''),
        # <br> 削除
        partial(re.sub, re.compile(r'<br.*?>'), ''),
        # {{foo|bar|ここを抽出}}
        partial(re.sub, re.compile(r'\{\{.*?([^|]+?)\}\}'), r'\1'),
    )
    info_dict = json.loads(sys.stdin.read())
    for k in info_dict.iterkeys():
        for partialsub in partialsubs:
            info_dict[k] = partialsub(info_dict[k])

    if len(sys.argv) > 1:
        for k, v in info_dict.iteritems():
            print u'{} = {}'.format(k, v)
    else:
        sys.stdout.write(json.dumps(info_dict))

# 公式国名 = United Kingdom of Great Britain and Northern Ireland
# ccTLD = .uk / .gb
# 首都 = ロンドン
# GDP値 = 2兆3162億
# 確立形態4 = 現在の国号「グレートブリテン及び北アイルランド連合王国」に変更

if __name__ == '__main__':
    main()
