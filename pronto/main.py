import preprocessing
import analyze
import display

text_file_name = '../data/story.txt'
vocabulary_file_name = '../data/vocabulary.txt'
stop_words = ['Momo', 'essere|stare']

story = preprocessing.file_to_string(text_file_name)
sentences = preprocessing.text_to_sentences(story)

vocabulary = preprocessing.file_to_string(vocabulary_file_name)

for sentence in sentences:
    tagged_sentence = preprocessing.tag_text(sentence)
    word_objects = analyze.tag_known_lemmas(vocabulary, stop_words, tagged_sentence)
    print(sentence + '\n' + str(analyze.ratio_of_known_words_to_all_words_in_text(word_objects)) + '% of the sentence should be comprehensible')
    print('New words:')
    for word in word_objects:
        if word.known is False:
            print(word.lemma)
    #analyze.translate_lemmas(unknowns)
    print('\n')