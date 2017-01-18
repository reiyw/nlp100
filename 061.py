#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import plyvel


def main():
    db = plyvel.DB('./db/')
    print db.get(sys.argv[1])

# % src/061.py "Al Street"
# United States

if __name__ == '__main__':
    main()
