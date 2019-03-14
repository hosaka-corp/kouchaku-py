#!/usr/bin/python3
# coding: utf-8
''' common_forms.py
Use MeCab to instantiate some common/special morpheme objects.
'''

from tokenize import *
from bunpo import *

# For some common forms, we can hack it and run a single, independent element 
# through MeCab in order to automatically obtain the right details. 

NAI     = getMorpheme("ない")
MASU    = getMorpheme("ます")
DESU    = getMorpheme("です")
TA      = getMorpheme("た")

# For other elements, in the abscence of a certain context, MeCab might not
# return the details that we want. In this case, we can just manually invoke
# MeCab (outside of this program) and manually create a set of details.

N       = nVerb({ 'surface': 'ん', 
            'pos': '助動詞', 
            'sub1': None, 
            'sub2': None, 
            'sub3': None, 
            'infl': '不変化型',
            'conj': '基本形',
            'root': 'ん', 
            'reading': 'ン', 
            'hatsuon': 'ン',
        })

