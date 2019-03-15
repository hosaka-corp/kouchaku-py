#!/usr/bin/python3
# coding: utf-8

''' conjugate.py
Abstract away all of the complicated transformations on verbs (as whole words).
Give users some simple functions that transform the characteristics of an
entire words (ie. tense, politeness, polarity, etc).
'''

from kouchaku.common import *

from kouchaku.tokenize import getMorpheme
from kouchaku.word import word

from kouchaku.aux_verb import masu, desu, ta, nVerb
from kouchaku.i_adj import nai
from kouchaku.verb import aru

def plainPast(root):
    w = word(getMorpheme(root))
    w.inflect(CONJUNCTIVE)
    w.append(ta())
    return w

def plainNegative(root):
    w = word(getMorpheme(root))
    w.inflect(IMPERFECTIVE)
    w.append(nai())
    return w

def plainNegativePast(root):
    w = word(getMorpheme(root))
    w.inflect(IMPERFECTIVE)
    w.append(nai())
    w.inflect(CONJUNCTIVE)
    w.append(aru())
    w.inflect(CONJUNCTIVE)
    w.append(ta())
    return w

def polite(root):
    w = word(getMorpheme(root))
    w.inflect(CONJUNCTIVE)
    w.append(masu())
    return w

def politePast(root):
    w = word(getMorpheme(root))
    w.inflect(CONJUNCTIVE)
    w.append(masu())
    w.inflect(CONJUNCTIVE)
    w.append(ta())
    return w

def politeNegative(root):
    w = word(getMorpheme(root))
    w.inflect(CONJUNCTIVE)
    w.append(masu())
    w.inflect(IMPERFECTIVE)
    w.append(nVerb())
    return w

def politeNegativePast(root):
    w = word(getMorpheme(root))
    w.inflect(CONJUNCTIVE)
    w.append(masu())
    w.inflect(IMPERFECTIVE)
    w.append(nVerb())
    w.append(desu())
    w.inflect(CONJUNCTIVE)
    w.append(ta())
    return w
