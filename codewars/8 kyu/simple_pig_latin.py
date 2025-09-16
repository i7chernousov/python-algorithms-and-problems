"""
Move the first letter of each word to the end of it,
then add "ay" to the end of the word.
Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""


def pig_it(text: str):
    """Функция переносит первую букву каждого слова в конец и добавляет текст ay"""
    word_list = text.split()
    result_word = []
    for word in word_list:
        if str(word).isalpha():
            result_word.append(word[1:] + word[:1] + "ay")
        else:
            result_word.append(word)

    return " ".join(result_word)



if __name__ == "__main__":
    print(pig_it("Pig latin is cool"))
    print(pig_it("Hello world !"))

