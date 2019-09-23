from googletrans import Translator
import preprocessing


def ratioOfKnownWordsToAllLemmasInText(vocabulary, text):
    knownWords = 0

    for word in text:
        if word in vocabulary:
            knownWords += 1

    ratio = knownWords / len(text) * 100

    return ratio


def orderSentencesByComprehension(vocabulary, sentences):
    sentencesWithComprehensionRatios = []

    for sentence in sentences:
        lemmatizedSentence = preprocessing.lemmatizeText(sentence)
        ratio = ratioOfKnownWordsToAllLemmasInText(vocabulary, lemmatizedSentence)
        sentencesWithComprehensionRatios.append([sentence, lemmatizedSentence, ratio])

        sentencesWithComprehensionRatiosOrderedByAsc = sorted(sentencesWithComprehensionRatios, key=lambda x: float(x[2]))

    return sentencesWithComprehensionRatiosOrderedByAsc


def getUnKnownWords(vocabulary, text):
    unknownWords = []

    for word in text:
        if word in vocabulary:
            continue
        else:
            unknownWords.append(word)

    return unknownWords


def translateWords(italianWords):
    translator = Translator()
    translations = translator.translate(italianWords)

    for translation in translations:
        if translation.origin == translation.text:
            print(translation.origin + ' -> ?')
        else:
            print(translation.origin + ' -> ' + translation.text)

