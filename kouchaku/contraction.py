#!/usr/bin/python3
# coding: utf-8

from kouchaku.word import *

from kouchaku.verb import godanVerb
from kouchaku.aux_verb import ta, tsuVerb
from kouchaku.i_adj import *

''' ---------------------------------------------------------------------------
I think we also technically need a container to represent contractions that
occur between two elements.

If you look at MeCab output (i.e. for Godan verbs contracted to った), it's
technically broken into Vっ and た. Instead of implementing this in terms of
a "container" for pairs of elements in a word, you might just consider having
"extra surfaces" that resolve to the final form.
'''

def checkClass(x, c1, y, c2):
    if ((isinstance(x, c1)) and (isinstance(y, c2))):
        return True
    else:
        return None

def checkContractionPair(x, y):
    """ If we find a contraction, return the contraction type. Note that Godan 
    verbs do not contract when the consonant is in the す row.
    """

    if (checkClass(x, godanVerb, y, ta)):
        if (x._consonant != 'す'):
            return GODAN_TA

    if (checkClass(x, godanVerb, y, tsuVerb)):
        if (x._consonant != 'す'):
            return GODAN_TSU

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

        if (self.type == GODAN_TSU):
            surface     = self.morphemes[0]._stem
            cons        = self.morphemes[0]._consonant
            if (cons == 'く'):
                surface += 'いて'
            elif (cons == 'ぐ'):
                surface += 'いで'
            elif ((cons == 'ぬ') or (cons == 'ぶ') or (cons == 'む')):
                surface += 'んで'
            elif ((cons == 'う') or (cons == 'つ') or (cons == 'る')):
                surface += 'って'
            return surface

        if (self.type == NAKATTA):
            surface     = 'なかった'
            return surface

