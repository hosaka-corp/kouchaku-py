#!/usr/bin/python3
# coding: utf-8

''' i_adj.py
Define all special i-adjectives (i.e. ない and maybe others later).
'''

from kouchaku.morpheme import iAdjective
from kouchaku.common import *


nai_detail = { 
    'surface': 'ない', 
    'pos': '形容詞', 
    'sub1': '自立', 
    'sub2': None, 
    'sub3': None, 
    'infl': '形容詞・アウオ段',
    'conj': '基本形',
    'root': 'ない', 
    'reading': 'ナイ', 
    'hatsuon': 'ナイ',
}

class nai(iAdjective):
    def __init__(self):
        super(nai, self).__init__(nai_detail)
        self._stem          = self.surface[:-1]


