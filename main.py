import preprocessing
import analyze
import colorama
import re
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


text_file_name = 'story.txt'
vocabulary_file_name = 'vocabulary.txt'

story = preprocessing.file_to_string(text_file_name)
sentences = preprocessing.text_to_sentences(story)

vocabulary = preprocessing.file_to_string(vocabulary_file_name)
tagged_vocabulary = preprocessing.tag_text(vocabulary)
lemmatized_vocabulary = set(preprocessing.lemmatize_text(tagged_vocabulary))

tagged_text = preprocessing.tag_text(sentences)

new_tags = analyze.tag_known_lemmas(lemmatized_vocabulary, tagged_text)

for tag in new_tags:
    if getattr(tag, 'known') is False:
        print(Back.RED + getattr(tag, 'word'), end=" ")
    else:
        print(getattr(tag, 'word'), end=" ")