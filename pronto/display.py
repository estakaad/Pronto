import colorama
from colorama import Fore, Back, Style
import re

colorama.init(autoreset=True)


#Input is list of word objects. Prints all words, unknown words being marked red.
def mark_unknown_words_red(words):
    for word in words:
        if word.known is False:
            print(Back.RED + word.word, end=' ')
        else:
            print(word.word, end=' ')


#Return dictionary of unknown nouns, verbs, adjectives, adverbs
def print_parts_of_speech(words):

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

    print(dict_pos)


#Print attributes of Word objects as sentences.
def print_objects_as_string(words):
    for i in range(len(words)):
        if i < len(words)-1:
            current = re.match("[^\w]", words[i].lemma)
            next = re.match("[^\w]", words[i+1].lemma)
            if current and next:
                print(words[i].word, end='')
            elif current is False and next is True:
                print(words[i].word, end='')
            elif current and next is False:
                print(words[i].word, end=' ')
        else:
            print(words[i].word)


#Print attributes of Word objects as sentences, all unknown words are printed red.
def print_unknown_words_red(words):
    for i in range(len(words)):
        if i < len(words)-1:
            z = re.match("[^\w]", words[i+1].word)
            if z:
                print(words[i].word, end='')
            else:
                if words[i].known == False:
                    print(Back.RED + words[i].word, end=' ')
                else:
                    print(words[i].word, end=' ')
        else:
            print(words[i].word)