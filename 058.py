#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
58. タプルの抽出

Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）に基づき，
「主語 述語 目的語」の組をタブ区切り形式で出力せよ．ただし，主語，述語，目的語の
定義は以下を参考にせよ．

- 述語: nsubj関係とdobj関係の子（dependant）を持つ単語
- 主語: 述語からnsubj関係にある子（dependent）
- 目的語: 述語からdobj関係にある子（dependent）
"""

import sys
from itertools import groupby

from lxml import etree
from corenlp_xml.dependencies import DependencyGraph


def main():
    tree = etree.parse(sys.stdin)
    for dependency in tree.iterfind('//dependencies[@type="collapsed-dependencies"]'):
        dg = DependencyGraph(dependency)
        for nsubj in dg.links_by_type('nsubj'):
            for dobj in dg.links_by_type('dobj'):
                if nsubj.governor.idx == dobj.governor.idx:
                    print '{}\t{}\t{}'.format(nsubj.dependent.text,
                                              nsubj.governor.text,
                                              dobj.dependent.text)
    return

    # (係り元id, 係り元の表層, 係り先の表層) のリスト
    # id で管理しないとうまくいかない例がある (3 文目)
    deps = []
    tree = etree.parse(sys.stdin)
    for dependencies in tree.iterfind('//dependencies[@type="collapsed-dependencies"]'):
        for dep in dependencies:
            dtype = dep.get('type')
            if dtype == 'nsubj' or dtype == 'dobj':
                deps.append((str(dep.find('governor').get('idx')),
                             dep.findtext('governor'),
                             dep.findtext('dependent')))

        for key, group in groupby(sorted(deps, key=lambda t: t[0]),
                                  key=lambda t:t[0]):
            partial_dep = list(group)
            if len(partial_dep) > 1:
                (_, predicate, subject), (_, _, object) = partial_dep
                print '{}\t{}\t{}'.format(subject, predicate, object)

        deps = []

# understanding   enabling        computers
# others  involve generation
# Turing  published       article
# experiment      involved        translation
# ELIZA   provided        interaction

if __name__ == '__main__':
    main()
