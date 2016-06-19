# -*- coding: utf-8 -*-
import sys,codecs,MeCab,re



def kana2gana(c):
    KXA = ord(u"ァ")
    KMI = ord(u"ミ")
    KMU = ord(u"ム")
    KNN = ord(u"ン")

    HXA = ord(u"ぁ")
    HMI = ord(u"み")
    HMU = ord(u"む")
    HNN = ord(u"ン")

    code = ord(c)
    after = code
    if KXA <= code <= KMI:
        after = code - KXA + HXA
    elif KMU <= code <= KNN:
        after = code - KMU + HMU
    return u"%c"%(after)

def kanas2ganas(s):
    after = u""
    for c in s:
        after += kana2gana(c)
    return after

def mec_parse(elems):
    A=elems.decode("utf-8").split()
    if len(A) != 2:
        return None
    phra,rest=A
    elems = rest.split(",")
    if len(elems) == 9:
        yomi = elems[7]
    elif len(elems) == 8:
        yomi = phra
    elif len(elems) == 7:
        yomi = phra
    else:
        return None
    yomi = kanas2ganas(yomi)
    return yomi

def yomi(word):
    all_yomi = ""
    m = MeCab.Tagger(' -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
    for mecline in m.parse(word.encode("utf-8")).split("\n"):
        if mecline == "EOS":
            break
        yomi = mec_parse(mecline)
        if yomi is None:
            break
        all_yomi += yomi
    return all_yomi

def wrap_yomi(word):
    return yomi(word)
