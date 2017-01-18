#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import cPickle

import plyvel


def main():
    if len(sys.argv) == 1:
        db = plyvel.DB('./db/', create_if_missing=True)
        with db.write_batch() as b:
            for line in sys.stdin:
                j = json.loads(line)
                name = j.get('name')
                tags = j.get('tags')
                if name is not None and tags is not None:
                    b.put(name.encode('utf-8'), cPickle.dumps(tags))
    else:
        db = plyvel.DB('./db/')
        tags = db.get(sys.argv[1])
        if tags is not None:
            tags = cPickle.loads(tags)
            for tag in tags:
                print '{}\t{}'.format(tag['value'], tag['count'])

# % zcat data/artist.json.gz | src/063.py
#
# % src/063.py "Peter P."
# punk    1
# germany 1

if __name__ == '__main__':
    main()
