from googletrans import Translator


def ratioOfKnownWordsToAllLemmasInText(vocabulary, text):
    knownWords = 0

    for word in text:
        if word in vocabulary:
            knownWords += 1

    ratio = knownWords / len(text) * 100

    return ratio


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

