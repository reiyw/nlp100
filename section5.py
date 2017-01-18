# -*- coding: utf-8 -*-

from itertools import groupby, ifilterfalse


class Line(object):
    EOS, CHUNK, MORPH = range(3)


class Morph(object):

    def __init__(self, line):
        self.surface, remain = line.strip().split('\t')
        self.pos, self.pos1, _, _, _, _, self.base = remain.split(',')[:7]

    def __str__(self):
        return '{surface}\t{base}\t{pos}\t{pos1}'.format(**self.__dict__)

    def __getitem__(self, item):
        # attr = 'surface'; morph[attr] で読み出せるようになる．
        # これをしないと getattr() とか使う必要があってちょっと面倒．
        return self.__dict__[item]


class Chunk(object):

    def __init__(self, chunk, morphs):
        # * {文節番号} {係り先}D x/x x
        ast, slf_str, dst_plus_D = chunk.split(' ')[:3]
        dst_str = dst_plus_D[:-1]

        self.slf = int(slf_str)
        self.dst = None if dst_str == '-1' else int(dst_str)
        self.morphs = [Morph(line) for line in morphs]
        self.srcs = []

    def __str__(self):
        s1 = '* 文節 {slf}: 係り先 {dst}, 係り元 {srcs}'.format(**self.__dict__)
        s2 = '\n'.join(morph.__str__() for morph in self.morphs)
        return '{}\n{}'.format(s1, s2)

    def valid(self):
        "記号だけからなる文節でなければ valid"
        return any(m.pos != '記号' for m in self.morphs)

    def surface(self):
        return ''.join(m.surface for m in self.morphs if m.pos != '記号')

    def base(self):
        return ''.join(m.base for m in self.morphs if m.pos != '記号')

    def contains(self, attr, query):
        return any(m[attr] == query for m in self.morphs)

    def match(self, *attr2query):
        if len(attr2query) == len(self.morphs):
            return all(m[attr] == query for m, (attr, query) in
                       zip(self.morphs, attr2query))

    def find(self, attr, query, reverse=False):
        for m in self.morphs if not reverse else reversed(self.morphs):
            if m[attr] == query:
                return m

    def replace_np(self, char):
        surfaces = ''.join(m.surface for m in self.morphs if
                           m.pos != '名詞' and m.pos != '記号')
        return '{char}{surfaces}'.format(**locals())


class Chunks(list):

    def __init__(self, *chunks):
        list.__init__(self, *chunks)

    def __str__(self):
        s1 = '-' * 40
        s2 = '\n'.join(chunk.__str__() for chunk in self)
        return '{}\n{}'.format(s1, s2)

    def valid(self):
        "valid な文節数が 1 より大きいなら true を返す．"
        return sum(chunk.valid() for chunk in self) > 1

    def surfaces(self):
        return [chunk.surface() for chunk in self if chunk is not None]


class Sentence(Chunks):

    def __init__(self, chunk2morphs):
        super(Sentence, self).__init__(Chunk(chunk, morphs) for chunk, morphs
                                       in chunk2morphs)

        # 係り先 Chunk の srcs に係り元の slf を追加
        for chunk in self:
            if chunk.dst is not None:
                self[chunk.dst].srcs.append(chunk.slf)

    def connect_path(self):
        res = [Path([c, self[c.dst]]) for c in self if c.dst is not None]
        return [p for p in res if p.valid()]

    def get(self, indexes):
        return Chunks([self[i] for i in indexes])

    def path_to_end(self, chunk):
        p = Path()
        p.append(chunk)
        while chunk.dst is not None:
            chunk = self[chunk.dst]
            p.append(chunk)
        return p


class Path(Chunks):

    def __init__(self, *chunks):
        super(Path, self).__init__(*chunks)


def classify_cabocha_line(line):
    if line == 'EOS\n':
        return Line.EOS
    elif line.startswith('* '):
        return Line.CHUNK
    else:
        return Line.MORPH


def parse_cabocha(cabocha_seq):
    """CaboCha の係り受け解析結果をパースする．

    Yields:
        Sentence オブジェクト
    """
    for startswith_eos, sentence in groupby(cabocha_seq,
                                            key=lambda l: l == 'EOS\n'):
        if not startswith_eos:
            # [chunk1, [morph11, morph12], chunk2, [morph21], ...]
            stripe = [next(g) if k == Line.CHUNK else list(g) for k, g in
                      groupby(sentence, key=classify_cabocha_line)]
            # [[chunk1, [morph11, morph12]], [chunk2, [morph21]], [...], ...]
            yield Sentence(zip(*[iter(stripe)]*2))


def unique_everseen(iterable, key=None):
    "List unique elements, preserving order. Remember all elements ever seen."
    # unique_everseen('AAAABBBCCDAABBB') --> A B C D
    # unique_everseen('ABBCcAD', str.lower) --> A B C D
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in ifilterfalse(seen.__contains__, iterable):
            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element
