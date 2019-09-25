import treetaggerwrapper
import re
from nltk import tokenize


class Word:
    def __init__(self, word, pos, lemma, known):
        self.word = word
        self.pos = pos
        self.lemma = lemma
        self.known = known


def fileToString(fileName):
    with open(fileName, 'r', encoding="utf-8") as file:
        stringOfText = file.read().replace('\n', ' ')
    return stringOfText


def textToSentences(text):
    sentences = tokenize.sent_tokenize(text)
    return sentences


def tagText(input):
    tagger = treetaggerwrapper.TreeTagger(TAGLANG='it')
    tags = tagger.tag_text(input)
    taggedInput = treetaggerwrapper.make_tags(tags)

    return taggedInput


#Input is a list of Tag objects. Returns a list of lemmas.
def lemmatizeText(tags):

    allLemmas = []

    for tag in tags:
        z = re.match("[^\w]", getattr(tag, 'lemma'))
        if z:
            continue
        else:
            allLemmas.append(getattr(tag, 'lemma'))

    return allLemmas


#Input is a list of lemmas as vocabulary and a list of Tag objects. Returns a list of Word objects.
#Word objects have an attribute 'known' which indicates whether the word is in the vocabulary.
def tagKnownLemmas(vocabulary, tags):

    newTags = []

    for tag in tags:
        z = re.match("[^\w]", getattr(tag, 'lemma'))
        if z:
            word = Word(getattr(tag, 'word'), getattr(tag, 'pos'), getattr(tag, 'lemma'), True)
            newTags.append(word)
        else:
            if getattr(tag, 'lemma') in vocabulary:
                word = Word(getattr(tag, 'word'), getattr(tag, 'pos'), getattr(tag, 'lemma'), True)
            else:
                word = Word(getattr(tag, 'word'), getattr(tag, 'pos'), getattr(tag, 'lemma'), False)
            newTags.append(word)

    return newTags