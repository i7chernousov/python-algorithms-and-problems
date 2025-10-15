"""
Напишите функцию, которая по заданной строке текста
(возможно, со знаками препинания и переносами строк)
возвращает массив из трех наиболее часто встречающихся слов,
в порядке убывания количества вхождений.
"""

def top_3_words(text: str):

    text = text.lower().translate(str.maketrans("", "", "-#\\,/.")).strip().split()

    duplicates = {}

    for word in text:
        if word in duplicates:
            duplicates[word] += 1
        else:
            duplicates[word] = 1

    top_words = []

    for _ in range(3):
        if not duplicates:
            break

        max_word = None
        max_count = 0

        for word, count in duplicates.items():
            if count > max_count:
                max_word = word
                max_count = count

        top_words.append(max_word)
        del duplicates[max_word]

    return top_words


if __name__ == '__main__':
    print(top_3_words("a a a  b  c c  d d d d  e e e e e"))












