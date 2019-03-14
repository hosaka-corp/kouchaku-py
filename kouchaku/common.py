#!/usr/bin/python3
# coding: utf-8

from enum import Enum

''' ---------------------------------------------------------------------------
Use Enums to make references to different properties of things somewhat easier.
You can avoid specifying the whole class if you add them to `globals()`.
'''

class inflectionType(Enum):
    IMPERFECTIVE    = 1
    CONJUNCTIVE     = 2
    DICTIONARY      = 3
    PERFECTIVE      = 4
    IMPERATIVE      = 5

class verbType(Enum):
    GODAN           = 1
    ICHIDAN         = 2
    AUX             = 4

class contractionType(Enum):
    GODAN_TA        = 1

# Nice hack for excluding Enum classname when using these
globals().update(inflectionType.__members__)
globals().update(verbType.__members__)
globals().update(contractionType.__members__)


''' ---------------------------------------------------------------------------
Big list of linguistic terminology used in mecab. You might want to find some 
way of tying this back to the EDICT tags for word types?
'''

terminology = {
    "接尾": "suffix",
    "名詞": "noun", 
    "助詞": "particle",
    "動詞": "verb", 
    "助動詞": "aux-v",
    "副詞": "adverb",
    "記号": "symbol",
    "形容詞": "i-adj",
    "連体詞": "adnom-adj", 
    "固有名詞": "prop-noun",
    "代名詞": "pronoun",
    "読点": "comma",
    "係助詞": "binding-particle",
    "終助詞": "ending-particle",
    "副助詞": "adverb-particle",
    "格助詞": "case-particle",
    "接続助詞": "conjunct-particle",
    "サ変接続": "suru-conjugation",
    "一段": "ichidan",
    "五段": "godan",
    "形容動詞語幹": "na-adjective",
    "副詞可能": "possible-adverb",
    "自立": "indep",
    "非自立": "dep",
    "一般": "common",
    "句点": "full-stop",
    "連体化": "attributive-change",
    "副詞化": "adverbial-change",
    "形容詞": "i-adjective",
    "基本形": "dictionary form",
    "助詞類接続": "connective-particle",
    "未然形": '-nai stem (imperfective/irrealis)',
    "連用形": '-masu stem (conjuctive/continuative)',
    "五段・ワ行促音便": "godan, wa-column sound change",
    "特殊・マス": "special case, -masu",
    "特殊・タ": "special case, -da",
    "サ変": "-sa-hen (-suru conjugation)",

}


''' ---------------------------------------------------------------------------
Hiragana tables.
Used for implementing inflection on Godan verbs, among other things.
'''

ctable = {
    'う': [ 'わ', 'い', 'う', 'え', 'お' ],
    'す': [ 'さ', 'し', 'す', 'せ', 'そ' ],
    'く': [ 'か', 'き', 'く', 'け', 'こ' ],
    'ぐ': [ 'が', 'ぎ', 'ぐ', 'げ', 'ご' ],
    'ず': [ 'ざ', 'じ', 'ず', 'せ', 'ぞ' ],
    'つ': [ 'た', 'ち', 'つ', 'て', 'と' ],
    'づ': [ 'だ', 'ぢ', 'づ', 'で', 'ど' ],
    'ぬ': [ 'な', 'に', 'ぬ', 'ね', 'の' ],
    'ふ': [ 'は', 'ひ', 'ふ', 'へ', 'ほ' ],
    'ぶ': [ 'ば', 'び', 'ぶ', 'べ', 'ぼ' ],
    'ぷ': [ 'ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ' ],
    'む': [ 'ま', 'み', 'む', 'め', 'も' ],
    'ゆ': [ 'や', None, 'ゆ', None, 'よ' ],
    'る': [ 'ら', 'り', 'る', 'れ', 'ろ' ],
}

kana_to_consonant= {
    'う': '0',
    'す': 's',
    'く': 'k',
    'ぐ': 'g',
    'ず': 'z',
    'つ': 't',
    'づ': 'd',
    'ぬ': 'n',
    'ふ': 'h',
    'ぶ': 'b',
    'ぷ': 'p',
    'む': 'm',
    'ゆ': 'y',
    'る': 'r',
}
