#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from nltk.stem import SnowballStemmer


@click.command()
@click.argument('file', type=click.File('r'))
def snowball_stemmer(file):
    stemmer = SnowballStemmer('english')
    for word in file:
        click.echo(stemmer.stem(word.strip()))


if __name__ == '__main__':
    snowball_stemmer()
