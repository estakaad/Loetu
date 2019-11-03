from estnltk import Text
from collections import Counter


def tokenize(content):

    text = Text(content)

    items = list(text.get.word_texts.postags.lemmas.as_zip)

    s = []
    v = []
    a = []
    d = []
    k = []

    for item in items:
        if item[1] == 'S':
            s.append(item[2])
        elif item[1] == 'V':
            v.append(item[2])
        elif item[1] == 'A':
            a.append(item[2])
        elif item[1] == 'D':
            d.append(item[2])
        elif item[1] == 'V':
            v.append(item[2])
        else:
            continue

    all_words = [s, v, a, d, k]

    return all_words


def count_words(words):
    print(Counter(words))