#!/usr/bin/env python
# -*- coding: utf-8 -*-

import plyvel


def main():
    db = plyvel.DB('./db/')
    print sum(1 for _, area in db.iterator() if area == 'Japan')

# 22128

if __name__ == '__main__':
    main()
