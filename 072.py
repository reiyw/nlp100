# 3 文字以上の英小文字と '-' からなる単語を使う
# % ruby -ane 'puts $F.select {|w| w =~ /^[a-z\-]{3,}$|\+1|-1/}.join(" ")' sentiment.txt > sentiment2.txt
# nltk モジュールからストップワードのリストを取得してファイルに吐き出す
# % python -c "[__import__('sys').stdout.write(word + ' ') for word in __import__('nltk').corpus.stopwords.words('english')]" > stopwords.txt
# ストップワード除去
# % ./rm_stopwords.py sentiment2.txt stopwords.txt > sentiment3.txt
# ステミング
# % ./snowball_stemmer.py sentiment3.txt > sentiment4.txt
# ここまでの処理で単語が消えた行があるのでそれを除去
# % grep -E '^[+\-]1.+' sentiment4.txt > sentiment5.txt

# 上の一連の処理を行うワンライナー．
# sentiment.txt を $1 にしてシェルスクリプトにできる．
# % grep -E '^[+\-]1.+' <(./snowball_stemmer.py <(./rm_stopwords.py <(ruby -ane 'puts $F.select {|w| w =~ /^[a-z\-]{3,}$|\+1|-1/}.join(" ")' sentiment.txt) stopwords.txt)) > sentiment5.txt


##### rm_stopwords.py #####


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import click


@click.command()
@click.option('-w', '--word', is_flag=True, help='one word per one line')
@click.argument('file', type=click.File('r'))
@click.argument('stopwords', type=click.File('r'))
def rm_stopwords(word, file, stopwords):
    s = set(stopwords.read().split())
    if word:
        [click.echo(word) for word in file if word not in s]
    else:
        for line in file:
            click.echo(' '.join(word for word in line.split() if word not in s))


if __name__ == '__main__':
    rm_stopwords()


##### snowball_stemmer.py #####


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from nltk.stem import SnowballStemmer


@click.command()
@click.option('-w', '--word', is_flag=True, help='one word per one line')
@click.argument('file', type=click.File('r'))
def snowball_stemmer(word, file):
    stemmer = SnowballStemmer('english')
    if word:
        [click.echo(stemmer.stem(word.strip())) for word in file]
    else:
        for line in file:
            click.echo(' '.join(stemmer.stem(word) for word in line.split()))


if __name__ == '__main__':
    snowball_stemmer()
