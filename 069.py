# % cd /path/to/069_bottle
# % python app.py
# http://localhost:8080/ で動くから curl で見る

##########
# app.py #
##########

# -*- coding: utf-8 -*-

import json

from bottle import run, get, post, request, view
from pymongo import MongoClient, DESCENDING


@get('/search')
def get_condition():
    return '''\
        <h1>hoge</h1>
        <form action="/search" method="post">
            <p>name: <input name="name" type="text" /></p>
            <p>aliases.name: <input name="aliases.name" type="text" /></p>
            <p>tags.value: <input name="tags.value" type="text" /></p>
            <p><input value="Search" type="submit" /></p>
        </form>
    '''


@post('/search')
@view('result.tpl')
def do_search():
    client = MongoClient()
    db = client.nlp100_ryot
    col = db.artist

    name= request.forms.get('name')
    aliases_name = request.forms.get('aliases.name')
    if aliases_name:
        aliases_name = [{'aliases.name': name.strip()}
                        for name in aliases_name.split(',')]
    else:
        aliases_name = []
    tags_value = request.forms.get('tags.value')
    if tags_value:
        tags_value = [{'tags.value': value.strip()}
                      for value in tags_value.split(',')]
    else:
        tags_value = []
    spec = {
        'name': request.forms.get('name'),
        '$and': aliases_name + tags_value,
    }
    spec = {k: v for k, v in spec.items() if v}
    return {'cursor': col.find(spec, sort=[('rating.value', DESCENDING)])}


run()


##############
# result.tpl #
##############

<table border=1>
  <tr>
    <th>rating.value</th>
    <th>rating.count</th>
    <th>name</th>
    <th>aliases.name</th>
    <th>area</th>
    <th>tags.value</th>
  </tr>
  % for item in cursor:
    <tr>
      % rating = item.get('rating')
      <td>{{rating['value'] if rating is not None else ''}}</td>
      <td>{{rating['count'] if rating is not None else ''}}</td>
      <td>{{item['name']}}</td>
      % aliases = item.get('aliases')
      % if aliases is not None:
        % aliases_name = ', '.join(alias['name'] for alias in aliases)
      % else:
        % aliases_name = ''
      % end
      <td>{{aliases_name}}</td>
      % area = item.get('area')
      % if area is None:
        % area = ''
      % end
      <td>{{area}}</td>
      % tags = item.get('tags')
      % if tags is not None:
        % tags_value = ', '.join(tag['value'] for tag in tags)
      % else:
        % tags_value = ''
      % end
      <td>{{tags_value}}</td>
    </tr>
  % end
</table>
