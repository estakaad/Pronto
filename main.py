import preprocessing
import analyze


textFileName = 'story.txt'
vocabularyFileName = 'vocabulary.txt'

story = preprocessing.fileToString(textFileName)
sentences = preprocessing.textToSentences(story)

vocabulary = preprocessing.fileToString(vocabularyFileName)
taggedVocabulary = preprocessing.tagText(vocabulary)
lemmatizedVocabulary = set(preprocessing.lemmatizeText(taggedVocabulary))

taggedText = preprocessing.tagText(sentences)

newTags = preprocessing.tagKnownLemmas(lemmatizedVocabulary, taggedText)

for tag in newTags:
    if getattr(tag, 'known') == False:
        print(getattr(tag, 'lemma') + ' - ' + str(getattr(tag, 'known')) + '\n')
