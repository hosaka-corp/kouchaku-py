#!/usr/bin/python3
# coding: utf-8

from kouchaku.conjugate import *

word = [ "会う", "登る", "遊ぶ", "話す", "飲む", "待つ",
        "上げる", "生きる",
]

for w in word:
    print("{} to {}".format(w, plainPast(w)))
    print("{} to {}".format(w, plainNegative(w)))
    print("{} to {}".format(w, plainNegativePast(w)))
    print("{} to {}".format(w, polite(w)))
    print("{} to {}".format(w, politePast(w)))
    print("{} to {}".format(w, politeNegative(w)))
    print("{} to {}".format(w, politeNegativePast(w)))
    print("{} to {}".format(w, continuative(w)))
    print()
