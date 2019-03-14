#!/usr/bin/python3
# coding: utf-8

''' test.py 
'''

from tokenize import *
from bunpo import *
from common_forms import *

w = word()
w.append(getMorpheme("乗る"))
w.inflect(CONJUNCTIVE)
w.append(MASU)
print("乗る\t → {}".format(w))

w = word()
w.append(getMorpheme("上げる"))
w.inflect(CONJUNCTIVE)
w.append(MASU)
w.inflect(CONJUNCTIVE)
w.append(TA)
print("あげる\t → {}".format(w))

w = word()
w.append(getMorpheme("話す"))
w.inflect(CONJUNCTIVE)
w.append(TA)
print("話す\t → {}".format(w))

w = word()
w.append(getMorpheme("待つ"))
w.inflect(IMPERFECTIVE)
w.append(NAI)
print("待つ\t → {}".format(w))

w = word()
w.append(getMorpheme("帰る"))
w.inflect(CONJUNCTIVE)
w.append(TA)
print("帰る\t → {}".format(w))

w = word()
w.append(getMorpheme("変える"))
w.inflect(CONJUNCTIVE)
w.append(TA)
print("変える\t → {}".format(w))

