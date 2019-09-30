import preprocessing
import analyze
import display


text_file_name = '../data/story.txt'
vocabulary_file_name = '../data/vocabulary.txt'
stop_words = ['essere|stare']

vocabulary = preprocessing.file_to_string(vocabulary_file_name)

story = preprocessing.file_to_string(text_file_name)
sentences = preprocessing.text_to_sentences(story)
tagged_sentence = preprocessing.tag_text(sentences)
word_objects = analyze.tag_known_lemmas(vocabulary, stop_words, tagged_sentence)
print('\n')
display.print_unknown_words_red(word_objects)