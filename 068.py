#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from pymongo import MongoClient, DESCENDING


def main():
    client = MongoClient()
    db = client.nlp100_ryot
    col = db.artist
    # fields は pymongo 3.0 で消えた
    for i, res in enumerate(col.find({'tags.value': 'dance'},
                                     fields=['name', 'rating.count'],
                                     sort=[('rating.count', DESCENDING)],
                                     limit=10),
                            start=1):
        print '{}\t{}\t{}'.format(i, res['rating']['count'], res['name'].encode('utf-8'))

# 1	26	Madonna
# 2	23	Björk
# 3	23	The Prodigy
# 4	15	Rihanna
# 5	13	Britney Spears
# 6	11	Maroon 5
# 7	7	Adam Lambert
# 8	7	Fatboy Slim
# 9	6	Basement Jaxx
# 10	5	Cornershop

if __name__ == '__main__':
    main()
