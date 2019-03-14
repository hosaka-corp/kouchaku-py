#!/usr/bin/python3
# coding: utf-8

from kouchaku.common import *

''' ---------------------------------------------------------------------------
In this model, a "morpheme" is a generic container for some meaningful element
in a word. In reality, a morpheme seems to be a finer-grained concept.
I can't find a closer word (other than "word"), so let's use this.
'''

class morpheme(object):
    def __init__(self, detail):
        self.prev       = None
        self.next       = None

        self.pos        = None
        self.inflection = None
        self._detail    = detail
        self.surface    = detail['root']

    def __str__(self):
        return self.surface



class iAdjective(morpheme):
    def __init__(self, detail):
        super(iAdjective, self).__init__(detail)
        self._stem          = self.surface[:-1]

    def inflect(self, base):
        if (base == IMPERFECTIVE):
            self.surface = self._stem + 'く'
            self.inflection = base
        elif (base == CONJUNCTIVE):
            self.surface = self._stem + 'く'
            self.inflection = base
        elif (base == DICTIONARY):
            self.surface = self._stem + 'い'
            self.inflection = base
        elif (base == PERFECTIVE):
            self.surface = self._stem + 'けれ'
            self.inflection = base
        elif (base == IMPERATIVE):
            self.surface = self._stem + 'かれ'
            self.inflection = base
        return self.surface



class particle(morpheme):
    def __init__(self, detail):
        super(particle, self).__init__(detail)
