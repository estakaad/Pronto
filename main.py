import preprocessing
import analyze


textFileName = 'story.txt'
vocabularyFileName = 'vocabulary.txt'

story = preprocessing.fileToString(textFileName)
storyList = preprocessing.lemmatizeText(story)

words = preprocessing.fileToString(vocabularyFileName)
wordList = preprocessing.lemmatizeText(words)
wordList = preprocessing.listOfUniqueLemmas(wordList)

ratioOfKnownToAllLemmas = analyze.ratioOfKnownWordsToAllLemmasInText(wordList, storyList)
print(str(ratioOfKnownToAllLemmas))

unknownWords = analyze.getUnKnownWords(wordList, storyList)
unknownWords = preprocessing.listOfUniqueLemmas(unknownWords)

print(story)

analyze.translateWords(unknownWords)