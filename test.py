#!/usr/bin/python3
# coding: utf-8

''' test.py 
'''

from kouchaku.conjugate import *

print("食べる becomes {}".format(plainPast("食べる")))
print("食べる becomes {}".format(plainNegative("食べる")))
print("食べる becomes {}".format(plainNegativePast("食べる")))

print("飲む becomes {}".format(plainPast("飲む")))
print("飲む becomes {}".format(plainNegative("飲む")))
print("飲む becomes {}".format(plainNegativePast("飲む")))
