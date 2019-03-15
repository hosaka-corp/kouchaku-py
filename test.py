#!/usr/bin/python3
# coding: utf-8

from kouchaku.conjugate import *

word = "飲む"

print("{} to {}".format(word, plainPast(word)))
print("{} to {}".format(word, plainNegative(word)))
print("{} to {}".format(word, plainNegativePast(word)))
print("{} to {}".format(word, polite(word)))
print("{} to {}".format(word, politePast(word)))
print("{} to {}".format(word, politeNegative(word)))
print("{} to {}".format(word, politeNegativePast(word)))
