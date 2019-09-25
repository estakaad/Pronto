from googletrans import Translator
import preprocessing
import re


class Word:
    def __init__(self, word, pos, lemma, known):
        self.word = word
        self.pos = pos
        self.lemma = lemma
        self.known = known


#Input is a list of lemmas as vocabulary and a list of Tag objects. Returns a list of Word objects.
#Word objects have an attribute 'known' which indicates whether the word is in the vocabulary.
def tag_known_lemmas(vocabulary, tags):

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


def ratio_of_known_words_to_all_words_in_text(vocabulary, text):
    knownWords = 0

    for word in text:
        if word in vocabulary:
            knownWords += 1

    ratio = knownWords / len(text) * 100

    return ratio


def order_sentences_by_comprehension(vocabulary, sentences):
    sentencesWithComprehensionRatios = []

    for sentence in sentences:
        lemmatizedSentence = preprocessing.lemmatizeText(sentence)
        ratio = ratioOfKnownWordsToAllLemmasInText(vocabulary, lemmatizedSentence)
        sentencesWithComprehensionRatios.append([sentence, lemmatizedSentence, ratio])

        sentencesWithComprehensionRatiosOrderedByAsc = sorted(sentencesWithComprehensionRatios, key=lambda x: float(x[2]))

    return sentencesWithComprehensionRatiosOrderedByAsc


def translate_words(italianWords):
    translator = Translator()
    translations = translator.translate(italianWords)

    for translation in translations:
        if translation.origin == translation.text:
            print(translation.origin + ' -> ?')
        else:
            print(translation.origin + ' -> ' + translation.text)

