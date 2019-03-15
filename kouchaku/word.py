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
        self.morphemes.append(m)

        # If there's only one element in the word, just add it and return
        if (len(self.morphemes) == 1):
            return self.morphemes

        # Always link the new element to the previous one
        self.morphemes[-1].prev = self.morphemes[-2]

        # Check and apply [potentially nested] contractions
        while (checkContractionPair(self.morphemes[-2], self.morphemes[-1])):
            y = self.morphemes.pop()
            x = self.morphemes.pop()
            self.morphemes.append(contractionPair(x, y))
            if (len(self.morphemes) == 1):
                return self.morphemes

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

