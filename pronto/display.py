import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)


#Input is list of word objects. Objects with known meaning are printed.
def mark_unknown_words_red(words):
    for word in words:
        if getattr(word, 'known') is False:
            print(Back.RED + getattr(word, 'word'), end=" ")
        else:
            print(getattr(word, 'word'), end=" ")


#Print unknown nouns, verbs, adjectives, adverbs
def print_parts_of_speech(words):

    dict_pos = {}
    dict_pos['Nouns'] = []
    dict_pos['Adjectives'] = []
    dict_pos['Verbs'] = []
    dict_pos['Adverbs'] = []

    for word in words:
        if getattr(word, 'known') is False:
            if (getattr(word, 'pos')) == 'NOM':
                dict_pos['Nouns'].append(getattr(word, 'lemma'))
            elif (getattr(word, 'pos')) == 'ADJ':
                dict_pos['Adjectives'].append(getattr(word, 'lemma'))
            elif (getattr(word, 'pos')).startswith('VER'):
                dict_pos['Verbs'].append(getattr(word, 'lemma'))
            elif (getattr(word, 'pos')) == 'ADV':
                dict_pos['Adverbs'].append(getattr(word, 'lemma'))
            else:
                continue

    print(dict_pos)
    #print(*set(pos), sep=' ')
