#!/usr/bin/python3
# coding: utf-8

from kouchaku.morpheme import morpheme
from kouchaku.common import *

''' ---------------------------------------------------------------------------
More generic classes of verbs can live here
'''

class verb(morpheme):
    def __init__(self, detail):
        super(verb, self).__init__(detail)
        self._stem          = self.surface[:-1]

class ichidanVerb(verb):
    def __init__(self, detail):
        super(ichidanVerb, self).__init__(detail)
        self._stem          = self.surface[:-1]

    def inflect(self, base):
        if (base == IMPERFECTIVE):
            self.surface = self._stem
            self.inflection = base
        elif (base == CONJUNCTIVE):
            self.surface = self._stem
            self.inflection = base
        elif (base == DICTIONARY):
            self.surface = self._stem + 'る'
            self.inflection = base
        elif (base == PERFECTIVE):
            self.surface = self._stem + 'れ'
            self.inflection = base
        elif (base == IMPERATIVE):
            self.surface = self._stem + 'ろ'
            self.inflection = base
        return self.surface


class godanVerb(verb):
    def __init__(self, detail):
        super(godanVerb, self).__init__(detail)
        self._consonant     = self.surface[-1:]
        self._stem          = self.surface[:-1]

    def inflect(self, base):
        if (base == IMPERFECTIVE):
            self.surface = self._stem + ctable[self._consonant][0]
            self.inflection = base
        elif (base == CONJUNCTIVE):
            self.surface = self._stem + ctable[self._consonant][1]
            self.inflection = base
        elif (base == DICTIONARY):
            self.surface = self._stem + ctable[self._consonant][2]
            self.inflection = base
        elif (base == PERFECTIVE):
            self.surface = self._stem + ctable[self._consonant][3]
            self.inflection = base
        elif (base == IMPERATIVE):
            self.surface = self._stem + ctable[self._consonant][4]
            self.inflection = base
        return self.surface

class auxVerb(morpheme):
    def __init__(self, detail):
        super(auxVerb, self).__init__(detail)


''' ---------------------------------------------------------------------------
I know there are a bunch of exceptional verbs, so let's define them here.
'''

aru_detail = { 
    'surface': 'ある', 
    'pos': '動詞', 
    'sub1': '自立', 
    'sub2': None, 
    'sub3': None, 
    'infl': '五段・ラ行',
    'conj': '基本形',
    'root': 'ある', 
    'reading': 'アル', 
    'hatsuon': 'アル',
}

class aru(godanVerb):
    def __init__(self):
        super(aru, self).__init__(aru_detail)

    def inflect(self, base):
        if (base == IMPERFECTIVE):
            self.surface = self._stem + 'ら'
            self.inflection = base
        elif (base == CONJUNCTIVE):
            self.surface = self._stem + 'り'
            self.inflection = base
        elif (base == DICTIONARY):
            self.surface = self._stem + 'る'
            self.inflection = base
        elif (base == PERFECTIVE):
            self.surface = self._stem + 'れ'
            self.inflection = base
        elif (base == IMPERATIVE):
            self.surface = self._stem + 'れ'
            self.inflection = base
        return self.surface


suru_detail = { 
    'surface': 'する', 
    'pos': '動詞', 
    'sub1': '自立', 
    'sub2': None, 
    'sub3': None, 
    'infl': '五段・ラ行',
    'conj': '基本形',
    'root': 'する', 
    'reading': 'スル', 
    'hatsuon': 'スル',
}

class suru(godanVerb):
    def __init__(self):
        super(suru, self).__init__(suru_detail)

    def inflect(self, base):
        if (base == IMPERFECTIVE):
            # Apparently this may be さ, せ, or し
            self.surface = 'さ'
            self.inflection = base
        elif (base == CONJUNCTIVE):
            self.surface = 'し'
            self.inflection = base
        elif (base == DICTIONARY):
            self.surface = self._stem + 'る'
            self.inflection = base
        elif (base == PERFECTIVE):
            self.surface = self._stem + 'れ'
            self.inflection = base
        elif (base == IMPERATIVE):
            self.surface = self._stem + 'れ'
            self.inflection = base
        return self.surface

