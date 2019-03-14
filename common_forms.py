#!/usr/bin/python3
# coding: utf-8
''' common_forms.py
Use MeCab to instantiate some common/special morpheme objects.
'''

from tokenize import *
from bunpo import *

NAI     = getMorpheme("ない")
MASU    = getMorpheme("ます")
TA      = getMorpheme("た")
