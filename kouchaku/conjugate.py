#!/usr/bin/python3
# coding: utf-8

''' conjugate.py
Abstract away all of the complicated transformations on verbs (as whole words).
Give users some simple functions that transform the characteristics of an
entire words (ie. tense, politeness, polarity, etc).
'''

from kouchaku.tokenize import *
from kouchaku.word import *
from kouchaku.common import *

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
