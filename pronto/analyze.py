from googletrans import Translator
import re


class Word:
    def __init__(self, word, pos, lemma, known):
        self.word = word
        self.pos = pos
        self.lemma = lemma
        self.known = known


#Input is a list of lemmas as vocabulary and a list of Tag objects. Returns a list of Word objects.
#Word objects have an attribute 'known' which indicates whether the word is in the vocabulary.
#Punctuation is considered as known. Proper names are considered known.
def tag_known_lemmas(vocabulary, stop_words, tags):
    new_tags = []

    for tag in tags:
        punctuation = re.match('[^\w]', tag.lemma)
        if punctuation:
            word = Word(tag.word, tag.pos, tag.lemma, True)
            new_tags.append(word)
        else:
            if tag.lemma in vocabulary:
                word = Word(tag.word, tag.pos, tag.lemma, True)
            elif tag.lemma in stop_words:
                word = Word(tag.word, tag.pos, tag.lemma, True)
            else:
                word = Word(tag.word, tag.pos, tag.lemma, False)
            new_tags.append(word)

    return new_tags


#Returns a dictionary where keys are parts of speech and values are lists of lemmas that belong to the POS.
## Includes only unknown words
def get_pos(words):
    #print('Creating a dictionary of nouns, adjectives, verbs and adverbs...')
    dict_pos = {}
    dict_pos['Nouns'] = []
    dict_pos['Adjectives'] = []
    dict_pos['Verbs'] = []
    dict_pos['Adverbs'] = []

    for word in words:
        if word.known is False:
            if word.pos == 'NOM':
                dict_pos['Nouns'].append(word.lemma)
            elif word.pos == 'ADJ':
                dict_pos['Adjectives'].append(word.lemma)
            elif word.pos.startswith('VER'):
                dict_pos['Verbs'].append(word.lemma)
            elif word.pos == 'ADV':
                dict_pos['Adverbs'].append(word.lemma)
            else:
                continue

    return dict_pos


def ratio_of_known_words_to_all_words_in_text(words):
    #print('Calculating ratio of known lemmas to all lemmas (excluding punctuation)...')
    known_count = sum(w.known is True for w in words)
    punct_count = sum(re.match('[^\w]', w.lemma) is True for w in words)
    ratio = (known_count - punct_count) / len(words) * 100

    return ratio


#Can't test because temporarily blocked by Google
def translate_lemmas(lemmas_in_italian):
    translator = Translator()

    translations = translator.translate(lemmas_in_italian)

    for translation in translations:
        if translation.origin == translation.text:
            print(translation.origin + '-> ?')
        else:
            print(translation.origin + ' -> ' + translation.text)

    return translation