#!/usr/bin/python3
# coding: utf-8

from kouchaku.word import *

from kouchaku.verb import godanVerb
from kouchaku.aux_verb import ta
from kouchaku.i_adj import *

''' ---------------------------------------------------------------------------
I think we also technically need a container to represent contractions that
occur between two elements.
'''

def checkClass(x, c1, y, c2):
    if ((isinstance(x, c1)) and (isinstance(y, c2))):
        return True
    else:
        return None

def checkContractionPair(x, y):
    """ If we find a contraction, return the contraction type """

    if (checkClass(x, godanVerb, y, ta)):
        return GODAN_TA

    if (checkClass(x, nai, y, contractionPair)):
        if ((x.inflection == CONJUNCTIVE) and (y.type == GODAN_TA)):
            return NAKATTA

    return None

class contractionPair(object):
    def __init__(self, x, y):
        self.type       = checkContractionPair(x, y)
        self.morphemes  = [x, y]
        self.surface    = self._createSurface()

    def _createSurface(self):
        if (self.type == GODAN_TA):
            surface     = self.morphemes[0]._stem
            cons        = self.morphemes[0]._consonant
            if (cons == 'く'):
                surface += 'いた'
            elif (cons == 'ぐ'):
                surface += 'いだ'
            elif ((cons == 'ぬ') or (cons == 'ぶ') or (cons == 'む')):
                surface += 'んだ'
            elif ((cons == 'う') or (cons == 'つ') or (cons == 'る')):
                surface += 'った'
            return surface
        if (self.type == NAKATTA):
            surface     = 'なかった'
            return surface
