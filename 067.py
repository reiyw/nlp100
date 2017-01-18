#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from pymongo import MongoClient


def main():
    client = MongoClient()
    db = client.nlp100_ryot
    col = db.artist
    for res in col.find({'aliases.name': sys.argv[1]}):
        print res['name']

# % src/067.py まみやみちお
# 間宮芳生

if __name__ == '__main__':
    main()
