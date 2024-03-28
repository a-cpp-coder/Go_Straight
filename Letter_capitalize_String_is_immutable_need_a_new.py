def LetterCapitalize(word: str) -> str:
    word_list = word.split(" ")
    result = ""

    for w in word_list:
        result += w[0].upper() + w[1:] + " "

    return result

print(LetterCapitalize("hello world"))

