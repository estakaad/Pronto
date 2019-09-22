import treetaggerwrapper
import re


def fileToString(fileName):
    with open(fileName, 'r', encoding="utf-8") as file:
        stringOfText = file.read().replace('\n', ' ')
    return stringOfText


def lemmatizeText(input):
    tagger = treetaggerwrapper.TreeTagger(TAGLANG='it')
    tags = tagger.tag_text(input)
    tags = treetaggerwrapper.make_tags(tags)

    allLemmas = []

    for tag in tags:
        z = re.match("[^\w]", getattr(tag, 'lemma'))
        if z:
            continue
        else:
            allLemmas.append(getattr(tag, 'lemma'))

    return allLemmas


def listOfUniqueLemmas(listOfAllLemmas):
    listOfUniqueLemmas = set(listOfAllLemmas)
    listOfUniqueLemmas = list(listOfUniqueLemmas)
    return listOfUniqueLemmas

