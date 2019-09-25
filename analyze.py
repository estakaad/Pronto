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

    new_tags = []

    for tag in tags:
        z = re.match("[^\w]", getattr(tag, 'lemma'))
        if z:
            word = Word(getattr(tag, 'word'), getattr(tag, 'pos'), getattr(tag, 'lemma'), True)
            new_tags.append(word)
        else:
            if getattr(tag, 'lemma') in vocabulary:
                word = Word(getattr(tag, 'word'), getattr(tag, 'pos'), getattr(tag, 'lemma'), True)
            else:
                word = Word(getattr(tag, 'word'), getattr(tag, 'pos'), getattr(tag, 'lemma'), False)
            new_tags.append(word)

    return new_tags


def ratio_of_known_words_to_all_words_in_text(vocabulary, text):
    known_words = 0

    for word in text:
        if word in vocabulary:
            known_words += 1

    ratio = known_words / len(text) * 100

    return ratio


def order_sentences_by_comprehension(vocabulary, sentences):
    sentences_with_comprehension_ratios = []

    for sentence in sentences:
        lemmatized_sentence = preprocessing.lemmatizeText(sentence)
        ratio = ratio_of_known_words_to_all_words_in_text(vocabulary, lemmatized_sentence)
        sentences_with_comprehension_ratios.append([sentence, lemmatized_sentence, ratio])

        sentencesWithComprehensionRatiosOrderedByAsc = sorted(sentences_with_comprehension_ratios, key=lambda x: float(x[2]))

    return sentencesWithComprehensionRatiosOrderedByAsc


def translate_words(italian_words):
    translator = Translator()
    translations = translator.translate(italian_words)

    for translation in translations:
        if translation.origin == translation.text:
            print(translation.origin + ' -> ?')
        else:
            print(translation.origin + ' -> ' + translation.text)