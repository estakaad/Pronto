import preprocessing
import analyze


textFileName = 'story.txt'
vocabularyFileName = 'vocabulary.txt'

story = preprocessing.fileToString(textFileName)
sentences = preprocessing.textToSentences(story)

words = preprocessing.fileToString(vocabularyFileName)
wordList = preprocessing.lemmatizeText(words)
wordList = preprocessing.listOfUniqueLemmas(wordList)

sentencesWithRatios = analyze.orderSentencesByComprehension(wordList, sentences)

for sentence in sentencesWithRatios:
    print(str(sentence[2]) + ' - ' + sentence[0])