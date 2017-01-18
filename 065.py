#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import MongoClient


def main():
    client = MongoClient()
    db = client.nlp100_ryot
    col = db.artist
    for queen in col.find({'name': 'Queen'}):
        print queen

# > db.artist.find({name: "Queen"})
# { "_id" : ObjectId("559e459793420c7463ff82c1"), "name" : "Queen", "tags" : [ { "count" : 1, "value" : "kamen rider w" }, { "count" : 1, "value" : "related-akb48" } ], "gender" : "Female", "area" : "Japan", "sort_name" : "Queen", "ended" : true, "gid" : "420ca290-76c5-41af-999e-564d7c71f1a7", "type" : "Character", "id" : 701492, "aliases" : [ { "name" : "Queen", "sort_name" : "Queen" } ] }
# { "_id" : ObjectId("559e459993420c746300496e"), "rating" : { "count" : 24, "value" : 92 }, "begin" : { "date" : 27, "year" : 1970, "month" : 6 }, "name" : "Queen", "tags" : [ { "count" : 2, "value" : "hard rock" }, { "count" : 1, "value" : "70s" }, { "count" : 1, "value" : "queen family" }, { "count" : 1, "value" : "90s" }, { "count" : 1, "value" : "80s" }, { "count" : 1, "value" : "glam rock" }, { "count" : 4, "value" : "british" }, { "count" : 1, "value" : "english" }, { "count" : 2, "value" : "uk" }, { "count" : 1, "value" : "pop/rock" }, { "count" : 1, "value" : "pop-rock" }, { "count" : 1, "value" : "britannique" }, { "count" : 1, "value" : "classic pop and rock" }, { "count" : 1, "value" : "queen" }, { "count" : 1, "value" : "united kingdom" }, { "count" : 1, "value" : "langham 1 studio bbc" }, { "count" : 1, "value" : "kind of magic" }, { "count" : 1, "value" : "band" }, { "count" : 6, "value" : "rock" }, { "count" : 1, "value" : "platinum" } ], "area" : "United Kingdom", "sort_name" : "Queen", "ended" : true, "gid" : "0383dadf-2a4e-4d10-a46a-e9e041da8eb3", "type" : "Group", "id" : 192, "aliases" : [ { "name" : "女王", "sort_name" : "女王" } ] }
# { "_id" : ObjectId("559e459e93420c74630203c6"), "name" : "Queen", "sort_name" : "Queen", "ended" : true, "gid" : "5eecaf18-02ec-47af-a4f2-7831db373419", "id" : 992994 }

# % src/065.py
# {u'name': u'Queen', u'area': u'Japan', u'gender': u'Female', u'tags': [{u'count': 1, u'value': u'kamen rider w'}, {u'count': 1, u'value': u'related-akb48'}], u'sort_name': u'Queen', u'ended': True, u'gid': u'420ca290-76c5-41af-999e-564d7c71f1a7', u'_id': ObjectId('559e459793420c7463ff82c1'), u'type': u'Character', u'id': 701492, u'aliases': [{u'name': u'Queen', u'sort_name': u'Queen'}]}
# {u'rating': {u'count': 24, u'value': 92}, u'begin': {u'date': 27, u'month': 6, u'year': 1970}, u'name': u'Queen', u'area': u'United Kingdom', u'tags': [{u'count': 2, u'value': u'hard rock'}, {u'count': 1, u'value': u'70s'}, {u'count': 1, u'value': u'queen family'}, {u'count': 1, u'value': u'90s'}, {u'count': 1, u'value': u'80s'}, {u'count': 1, u'value': u'glam rock'}, {u'count': 4, u'value': u'british'}, {u'count': 1, u'value': u'english'}, {u'count': 2, u'value': u'uk'}, {u'count': 1, u'value': u'pop/rock'}, {u'count': 1, u'value': u'pop-rock'}, {u'count': 1, u'value': u'britannique'}, {u'count': 1, u'value': u'classic pop and rock'}, {u'count': 1, u'value': u'queen'}, {u'count': 1, u'value': u'united kingdom'}, {u'count': 1, u'value': u'langham 1 studio bbc'}, {u'count': 1, u'value': u'kind of magic'}, {u'count': 1, u'value': u'band'}, {u'count': 6, u'value': u'rock'}, {u'count': 1, u'value': u'platinum'}], u'sort_name': u'Queen', u'ended': True, u'gid': u'0383dadf-2a4e-4d10-a46a-e9e041da8eb3', u'_id': ObjectId('559e459993420c746300496e'), u'type': u'Group', u'id': 192, u'aliases': [{u'name': u'\u5973\u738b', u'sort_name': u'\u5973\u738b'}]}
# {u'name': u'Queen', u'sort_name': u'Queen', u'ended': True, u'gid': u'5eecaf18-02ec-47af-a4f2-7831db373419', u'_id': ObjectId('559e459e93420c74630203c6'), u'id': 992994}


if __name__ == '__main__':
    main()
