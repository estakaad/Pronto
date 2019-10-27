import preprocessing
import analyze
import display
from nltk.corpus import wordnet

text_file_name = '../data/story.txt'
vocabulary_file_name = '../data/vocabulary.txt'
stop_words = ['essere|stare']

vocabulary = preprocessing.file_to_string(vocabulary_file_name)

story = preprocessing.file_to_string(text_file_name)
sentences = preprocessing.text_to_sentences(story)
tagged_sentence = preprocessing.tag_text(sentences)
word_objects = analyze.tag_known_lemmas(vocabulary, stop_words, tagged_sentence)
display.print_unknown_words_red(word_objects)

print('\n---------------------------\n')
ratio = analyze.ratio_of_known_words_to_all_words_in_text(word_objects)
print('%.2f' % ratio + '% of the text should be comprehensible.\n')

print('---------------------------\n')
print('List of new words with English equivalents from WordNet.\n')
display.print_new_words_with_synonyms(word_objects)

print('---------------------------\n')
print('List of new words with English translations from Google Translate.\n')
display.print_new_words_with_translations(word_objects)