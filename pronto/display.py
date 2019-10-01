import colorama
from colorama import Fore, Back, Style
import re
import analyze

colorama.init(autoreset=True)


#Input is list of word objects. Prints all words, unknown words being marked red.
def mark_unknown_words_red(words):
    for word in words:
        if word.known is False:
            print(Back.RED + word.word, end=' ')
        else:
            print(word.word, end=' ')


#Return dictionary of unknown nouns, verbs, adjectives, adverbs
def get_parts_of_speech_of_new_words(words):

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


#Print new words.
def print_new_words(words):
    parts_of_speech = get_parts_of_speech_of_new_words(words)

    print('New nouns (' + str(len(parts_of_speech.get('Nouns'))) + ')\n')
    if len(parts_of_speech.get('Nouns')) == 0:
        print('-')
    else:
        for noun in set(parts_of_speech.get('Nouns')):
            print(noun + ' - ' + analyze.get_synonyms(noun, 'noun'))

    print('\nNew verbs (' + str(len(parts_of_speech.get('Verbs'))) + ')\n')
    if len(parts_of_speech.get('Verbs')) == 0:
        print('-')
    else:
        for verb in set(parts_of_speech.get('Verbs')):
            print(verb + ' - ' + analyze.get_synonyms(verb, 'verb'))

    print('\nNew adjectives (' + str(len(parts_of_speech.get('Adjectives'))) + ')\n')
    if len(parts_of_speech.get('Adjectives')) == 0:
        print('-')
    else:
        for adj in set(parts_of_speech.get('Adjectives')):
            print(adj + ' - ' + analyze.get_synonyms(adj, 'adjective'))

    print('\nNew adverbs (' + str(len(parts_of_speech.get('Adverbs'))) + ')\n')
    if len(parts_of_speech.get('Adverbs')) == 0:
        print('-')
    else:
        for adv in set(parts_of_speech.get('Adverbs')):
            print(adv + ' - ' + analyze.get_synonyms(adv, 'adverb'))


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