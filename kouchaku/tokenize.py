#!/usr/bin/python3
# coding: utf-8

''' tokenize.py
Wrappers for nice interactions between MeCab and stuff in `bunpo.py`.
'''

import MeCab
from json import dumps

from kouchaku.word import *
from kouchaku.aux_verb import *
from kouchaku.verb import *

# Set up arguments to the MeCab binary
mecab = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/")

def getDetail(node):
    """ Given a MeCab node, produce a nice `dict` of features """
    feature = node.feature.split(sep=',')
    detail = {
        'surface':  node.surface,
        'pos':      feature[0] if (feature[0] != '*') else None,
        'sub1':     feature[1] if (feature[1] != '*') else None,
        'sub2':     feature[2] if (feature[2] != '*') else None,
        'sub3':     feature[3] if (feature[3] != '*') else None,
        'infl':     feature[4] if (feature[4] != '*') else None,
        'conj':     feature[5] if (feature[5] != '*') else None,
        'root':     feature[6] if (feature[6] != '*') else None,
        'reading':  feature[7] if (feature[7] != '*') else None,
        'hatsuon':  feature[8] if (feature[8] != '*') else None,
    }
    return detail

def getNode(surface):
    """ Give some surface element/s, return MeCab node objects """
    text = mecab.parse(surface)
    node = mecab.parseToNode(surface)
    return node


def getMorpheme(surface):
    """ Use MeCab to return a single morpheme object from input """
    node = getNode(surface)

    while node:
        if node.surface in [' ', '', '\n']:
            node = node.next
            continue

        detail = getDetail(node)
        if (detail['pos'] == 'BOS/EOS'):
            node = node.next
            continue
        #print(dumps(detail, indent=2, ensure_ascii=False))

        # Verbs
        if (detail['pos'] == '動詞'): 
            if ('一段' in detail['infl']):
                return ichidanVerb(detail)
            elif ('五段' in detail['infl']):
                return godanVerb(detail)

        elif (detail['pos'] == '助動詞'):
            if (('特殊' in detail['infl'])):
                if (detail['root'] == 'ます'):
                    return masu(detail)
                if (detail['root'] == 'た'):
                    return ta(detail)
                if (detail['root'] == 'です'):
                    return desu(detail)
            else:
                return auxVerb(detail)

        # i-adjectives
        elif (detail['pos'] == '形容詞'):
            return iAdjective(detail)
        else:
            print("Couldn't return a morpheme object for {}".format(surface))
            return None
        node = node.next


