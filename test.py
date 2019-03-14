#!/usr/bin/python3
# coding: utf-8

''' test.py 
'''

from tokenize import *
from bunpo import *
from common_forms import *

# Convert 食べる into 食べませんでした
root = "食べる"
w = word()
w.append(getMorpheme(root))
w.inflect(CONJUNCTIVE)
w.append(MASU)
w.inflect(IMPERFECTIVE)
w.append(N)
w.append(DESU)
w.inflect(CONJUNCTIVE)
w.append(TA)
print("{}\t → {}".format(root, w))
