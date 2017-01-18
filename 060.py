#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json

import plyvel


def main():
    db = plyvel.DB('./db/', create_if_missing=True)
    with db.write_batch() as b:
        for line in sys.stdin:
            j = json.loads(line)
            key = j.get('name')
            value = j.get('area')
            if key is not None and value is not None:
                b.put(key.encode('utf-8'), value.encode('utf-8'))

# % zcat data/artist.json.gz | src/060.py

if __name__ == '__main__':
    main()
