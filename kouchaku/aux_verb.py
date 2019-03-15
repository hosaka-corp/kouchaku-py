#!/usr/bin/python3
# coding: utf-8

''' aux_verb.py
Define all relevant auxiliary verbs that behave in some exceptional way.
'''

from kouchaku.verb import auxVerb
from kouchaku.common import *

masu_detail = {
    'surface':      'ます',
    'pos':          '助動詞',
    'sub1':         None,
    'sub2':         None,
    'sub3':         None,
    'infl':         '特殊・マス',
    'conj':         '基本形',
    'root':         'ます',
    'reading':      'マス',
    'hatsuon':      'マス',
}

class masu(auxVerb):
    def __init__(self):
        super(masu, self).__init__(masu_detail)
        self._stem = self.surface[:-1]

    def inflect(self, base):
        if (base == IMPERFECTIVE):
            self.surface = self._stem + 'せ'
            self.inflection = base
        elif (base == CONJUNCTIVE):
            self.surface = self._stem + 'し'
            self.inflection = base
        elif (base == DICTIONARY):
            self.surface = self._stem + 'す'
            self.inflection = base
        elif (base == PERFECTIVE):
            self.surface = self._stem + 'せ'
            self.inflection = base
        elif (base == IMPERATIVE):
            self.surface = self._stem + 'せ'
            self.inflection = base
        return self.surface


ta_detail = {
    'surface':      'た',
    'pos':          '助動詞',
    'sub1':         None,
    'sub2':         None,
    'sub3':         None,
    'infl':         '特殊・タ',
    'conj':         '基本形',
    'root':         'た',
    'reading':      'タ',
    'hatsuon':      'タ',
}


class ta(auxVerb):
    def __init__(self):
        super(ta, self).__init__(ta_detail)
        self._stem = self.surface

    def inflect(self, base):
        if (base == IMPERFECTIVE):
            self.surface = self._stem + 'ろ'
            self.inflection = base
        elif (base == DICTIONARY):
            self.surface = self._stem
            self.inflection = base
        elif (base == PERFECTIVE):
            self.surface = self._stem + 'ら'
            self.inflection = base
        return self.surface


desu_detail = {
    'surface':      'です',
    'pos':          '助動詞',
    'sub1':         None,
    'sub2':         None,
    'sub3':         None,
    'infl':         '特殊・デス',
    'conj':         '基本形',
    'root':         'です',
    'reading':      'デス',
    'hatsuon':      'デス',
}

class desu(auxVerb):
    def __init__(self, detail=None):
        super(desu, self).__init__(desu_detail)
        self._stem          = self.surface[:-1]

    def inflect(self, base):
        if (base == IMPERFECTIVE):
            self.surface = self._stem + 'しょ'
            self.inflection = base
        elif (base == CONJUNCTIVE):
            self.surface = self._stem + 'し'
            self.inflection = base
        elif (base == DICTIONARY):
            self.surface = self._stem + 'す'
            self.inflection = base
        return self.surface



nVerb_detail = {
    'surface':      'ん',
    'pos':          '助動詞',
    'sub1':         None,
    'sub2':         None,
    'sub3':         None,
    'infl':         '不変化型',
    'conj':         '基本形',
    'root':         'ん',
    'reading':      'ン',
    'hatsuon':      'ン',
}

class nVerb(auxVerb):
    """ In Pomax' book, ん is treated as the modern dictionary/attributive
    form of an auxiliary verb for negation (an abbreviation of the classical
    verb ぬ). By itself, MeCab seems to treat ん as a sentence-final particle,
    although in the context of ません, it is properly tagged as an auxiliary.
    """

    def __init__(self, detail=None):
        super(nVerb, self).__init__(nVerb_detail)
        self._stem          = self.surface

    def inflect(self, form):
        pass

