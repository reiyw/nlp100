#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json

from pymongo import MongoClient


def main():
    client = MongoClient()
    db = client.nlp100_ryot
    col = db.artist
    col.insert([json.loads(line) for line in sys.stdin])
    col.create_index('name')
    col.create_index('aliases.name')
    col.create_index('tags.value')
    col.create_index('rating.value')

# zcat data/artist.json.gz | src/064.py

if __name__ == '__main__':
    main()
