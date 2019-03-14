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

def checkContractionPair(x, y):
    """ Only checks 'x' with the terminal element.
    Returns some value in the contractionType enum.
    Returns None if no contraction has been applied.
    """
    # Contractions between Godan verbs and the た auxiliary when the verb is
    # in the conjunctive form. This doesn't occur with verbs that end in す.
    if ((isinstance(x, godanVerb)) and (isinstance(y, ta)) 
            and (x._consonant != 'す') and (x.inflection == CONJUNCTIVE)):
        return GODAN_TA
    else:
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


