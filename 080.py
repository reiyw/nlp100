#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def main():
    for line in sys.stdin:
        words_may_contain_empty = [
            w.strip('.,!?;:()[]\'"') for w in line.split()
        ]
        words = [word for word in words_may_contain_empty if word]
        if words:
            print ' '.join(words)


if __name__ == '__main__':
    main()
