#!/usr/bin/python3
# coding: utf-8

from enum import Enum
from english_defs import *

''' ---------------------------------------------------------------------------
Use Enums to make references to different properties of things somewhat easier.
You can avoid specifying the whole class if you add them to `globals()`.
'''

class inflectionType(Enum):
    IMPERFECTIVE    = 1
    CONJUNCTIVE     = 2
    DICTIONARY      = 3
    PERFECTIVE      = 4
    IMPERATIVE      = 5

class verbType(Enum):
    GODAN           = 1
    ICHIDAN         = 2
    AUX             = 4

class contractionType(Enum):
    GODAN_TA        = 1

# Nice hack for excluding Enum classname when using these
globals().update(inflectionType.__members__)
globals().update(verbType.__members__)
globals().update(contractionType.__members__)


''' ---------------------------------------------------------------------------
In this model, a "morpheme" is a generic container for some meaningful element
in a word. In reality, a morpheme seems to be a finer-grained concept.
I can't find a closer word (other than "word"), so let's use this.

Classes for types of verbs (and verbal adjectives) should be derived from this.
We're assuming [for now] that we get input in the dictionary form.

Each class of verb should have a generic set of inflections.
For outliers with exceptional behaviour, I think [right now] we're doomed to
create new unique classes (because of the way I implemented inflection)?
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

class ichidanVerb(morpheme):
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

class godanVerb(morpheme):
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

class auxVerb(morpheme):
    def __init__(self, detail):
        super(auxVerb, self).__init__(detail)

class masu(auxVerb):
    def __init__(self, detail):
        super(masu, self).__init__(detail)
        self._stem          = self.surface[:-1]

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

class ta(auxVerb):
    def __init__(self, detail):
        super(ta, self).__init__(detail)
        self._stem          = self.surface

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

''' ---------------------------------------------------------------------------
I think we also technically need a container to represent contractions that
occur between two elements.

There will probably be issues with this later on :^)
'''

def checkContractionPair(x, y):
    """ Only checks 'x' with the terminal element.
    Returns some value in the contractionType enum.
    Returns None if no contraction has been applied.
    """
    # Contractions between Godan verbs and the た auxiliary.
    # This doesn't occur with Godan verbs that end in す.
    if ((isinstance(x, godanVerb)) and (isinstance(y, ta)) and (x._consonant != 'す')):
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
    def __init__(self):
        self.morphemes  = []
        self.pos        = None

    def __str__(self):
        s = str()
        for m in self.morphemes:
            s += m.surface
        return s

    def append(self, *args):
        for m in args:

            # Link the new morpheme to the one at the end of the list
            if (len(self.morphemes) >= 1):
                m.prev = self.morphemes[-1]

                # Potentially insert a contractionPair
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

    def _doContraction(self, y):
        """ Only checks 'x' with the terminal element.
        Returns True if we've modified the list, otherwise return None.
        """
        if (checkContractionPair(self.morphemes[-1], y)):
            x = self.morphemes.pop()
            c = contractionPair(x, y)
            self.morphemes.append(c)
            return True
        else:
            return None

