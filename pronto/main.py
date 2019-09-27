import preprocessing
import analyze
import display

text_file_name = '../data/story.txt'
vocabulary_file_name = '../data/vocabulary.txt'
stop_words = ['Momo']

story = preprocessing.file_to_string(text_file_name)
sentences = preprocessing.text_to_sentences(story)

vocabulary = preprocessing.file_to_string(vocabulary_file_name)
tagged_vocabulary = preprocessing.tag_text(vocabulary)
lemmatized_vocabulary = set(preprocessing.lemmatize_text(tagged_vocabulary))

tagged_text = preprocessing.tag_text(sentences)

new_tags = analyze.tag_known_lemmas(lemmatized_vocabulary, stop_words, tagged_text)

display.mark_unknown_words_red(new_tags)
print('\n')
display.print_parts_of_speech(new_tags)