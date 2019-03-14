#!/usr/bin/python3
# coding: utf-8

from enum import Enum

from kouchaku.common import *
from kouchaku.contraction import *
from kouchaku.morpheme import *

''' ---------------------------------------------------------------------------
As far as I can tell, the two main operations on verbs are:

        - Appending other elements
        - Inflecting the terminal element

It seems like the notion of "word" in Japanese is very hazy. Right now, I'm
mostly interested in verbs. I'm not sure if a "verb" is exactly a "word" by
definition in this case, which makes things somewhat confusing for me.

In the context of a sentence, words take on a "part-of-speech." However, in
the analysis of Japanese verbs, it seems like there are sometimes various
components (but not standalone words themselves) which are best described as
having a part-of-speech. There are also a bunch of exceptional, auxiliary
verbs which are used to make certain distinctions.

This seems to suggest that "part-of-speech" is more atomic property of some
parts of a word, and that the final "part-of-speech" given to the "whole word"
is probably seperate in some cases.
'''

class word(object):
    def __init__(self, root=None):
        self.morphemes  = []
        self.pos        = None

        if (root):
            self.append(root)

    def __str__(self):
        s = str()
        for m in self.morphemes:
            s += m.surface
        return s

    def append(self, m):
        # Link the new morpheme to the one at the end of the list
        if (len(self.morphemes) >= 1):
            m.prev = self.morphemes[-1]

            # Potentially insert a contraction
            if(self._doContraction(m)):
                return self.morphemes

        self.morphemes.append(m)
        return self.morphemes

    def pop(self):
        return self.morphemes.pop()
        # If the terminal object is a contraction, put the first element back
        #if (isinstance(self.morphemes[-1], contractionPair)):
        #else:
        #    return self.morphemes.pop()

    def inflect(self, form):
        """ Inflect the terminal element in the word """
        self.morphemes[-1].inflect(form)

    def _doContraction(self, m):
        """ Only checks 'x' with the terminal element.
        Returns True if we've modified the list, otherwise return None.
        """
        if (checkContractionPair(self.morphemes[-1], m)):
            x = self.morphemes.pop()
            c = contractionPair(x, m)
            self.morphemes.append(c)
            return True
        else:
            return None

