import treetaggerwrapper
import re
from nltk import tokenize


def file_to_string(fileName):
    with open(fileName, 'r', encoding="utf-8") as file:
        stringOfText = file.read().replace('\n', ' ')
    return stringOfText


def text_to_sentences(text):
    sentences = tokenize.sent_tokenize(text)
    return sentences


def tag_text(input):
    tagger = treetaggerwrapper.TreeTagger(TAGLANG='it')
    tags = tagger.tag_text(input)
    taggedInput = treetaggerwrapper.make_tags(tags)

    return taggedInput


#Input is a list of Tag objects. Returns a list of lemmas.
def lemmatize_text(tags):

    allLemmas = []

    for tag in tags:
        z = re.match("[^\w]", getattr(tag, 'lemma'))
        if z:
            continue
        else:
            allLemmas.append(getattr(tag, 'lemma'))

    return allLemmas


