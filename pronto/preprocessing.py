import treetaggerwrapper
import re
from nltk import tokenize


def file_to_string(file_name):
    #print('Reading from file ' + file_name + '...')
    with open(file_name, 'r', encoding="utf-8") as file:
        string_of_text = file.read().replace('\n', ' ')
    return string_of_text

#Returns a list of sentences
def text_to_sentences(text):
    #print('Splitting text to sentences...')
    sentences = tokenize.sent_tokenize(text)
    return sentences


def tag_text(input):
    #print('Creating Tag objects from text...')
    tagger = treetaggerwrapper.TreeTagger(TAGLANG='it')
    tags = tagger.tag_text(input)
    tagged_input = treetaggerwrapper.make_tags(tags)
    return tagged_input


#Input is a list of Tag objects. Returns a list of lemmas.
def lemmatize_text(tags):
    #print('Creating a list of lemmas from a list of Tag objects...')
    all_lemmas = []

    for tag in tags:
        z = re.match("[^\w]", tag.lemma)
        if z:
            continue
        else:
            all_lemmas.append(tag.lemma)

    return all_lemmas