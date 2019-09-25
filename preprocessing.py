import treetaggerwrapper
import re
from nltk import tokenize


def file_to_string(file_name):
    with open(file_name, 'r', encoding="utf-8") as file:
        string_of_text = file.read().replace('\n', ' ')
    return string_of_text


def text_to_sentences(text):
    sentences = tokenize.sent_tokenize(text)
    return sentences


def tag_text(input):
    tagger = treetaggerwrapper.TreeTagger(TAGLANG='it')
    tags = tagger.tag_text(input)
    tagged_input = treetaggerwrapper.make_tags(tags)

    return tagged_input


#Input is a list of Tag objects. Returns a list of lemmas.
def lemmatize_text(tags):

    all_lemmas = []

    for tag in tags:
        z = re.match("[^\w]", getattr(tag, 'lemma'))
        if z:
            continue
        else:
            all_lemmas.append(getattr(tag, 'lemma'))

    return all_lemmas


#Add stopwords...