#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""20. JSONデータの読み込み

Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を
表示せよ．以降の処理は，この記事本文に対して処理を実行せよ．
"""

import sys
import gzip
import json


def main():
    # class gzip.GzipFile([filename[, mode[, compresslevel[, fileobj[, mtime]]]]])
    #   GzipFile クラスのコンストラクタ． GzipFile オブジェクトは readinto() と
    #   truncate() メソッドを除くほとんどのファイルオブジェクトのメソッドを
    #   シミュレートする．
    for line in gzip.GzipFile(fileobj=sys.stdin):
        # json モジュールは Unicode 文字列にデコードする
        an_article = json.loads(line)
        # Unicode 型と str 型を比較するときは str 型が Unicode 型に変換されるが
        # すべての文字のコードポイントが 128 未満なら問題なし．
        # str 文字列と Unicode 文字列の内部表現はそれぞれ UTF-8 と UTF-32 ？
        if an_article['title'] == u'イギリス':
            sys.stdout.write(an_article['text'].encode('utf-8'))
            break


if __name__ == '__main__':
    main()
