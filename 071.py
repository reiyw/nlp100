#!/usr/bin/env python
# -*- coding: utf-8 -*-

my_stoplist = {'i', 'we', 'you', 'he', 'she', 'they', 'it'}


def is_stopword(word, stoplist=my_stoplist):
    return word in stoplist


def test(word, stoplist=my_stoplist):
    if stoplist is None:
        print '{}\t{}'.format(word, 'o' if is_stopword(word) else 'x')
    else:
        print '{}\t{}'.format(word, 'o' if is_stopword(word, stoplist) else 'x')


def main():
    test('we')
    test('them')

# we	o
# them	x

if __name__ == '__main__':
    main()
