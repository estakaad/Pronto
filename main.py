import preprocessing
import analyze


textFileName = 'story.txt'
vocabularyFileName = 'vocabulary.txt'

story = preprocessing.file_to_string(textFileName)
sentences = preprocessing.text_to_sentences(story)

vocabulary = preprocessing.file_to_string(vocabularyFileName)
taggedVocabulary = preprocessing.tag_text(vocabulary)
lemmatizedVocabulary = set(preprocessing.lemmatize_text(taggedVocabulary))

taggedText = preprocessing.tag_text(sentences)

newTags = analyze.tag_known_lemmas(lemmatizedVocabulary, taggedText)

for tag in newTags:
    if getattr(tag, 'known') == False:
        print(getattr(tag, 'lemma') + ' - ' + str(getattr(tag, 'known')))
