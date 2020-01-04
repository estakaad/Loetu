from estnltk import Text
from collections import Counter


#Tokenize content.
def tokenize(content):
    text = Text(content)
    items = list(text.get.word_texts.postags.lemmas.as_zip)

    s = []
    v = []
    a = []

    for item in items:
        if item[1] == 'S':
            s.append(item[2])
        elif item[1] == 'V':
            v.append(item[2])
        elif item[1] == 'A':
            a.append(item[2])
        else:
            continue

    all_lemmas = [s, v, a]

    return all_lemmas


def get_list_of_subst(all_lemmas):
    subst = all_lemmas[0]
    return subst


def get_list_of_verbs(all_lemmas):
    verbs = all_lemmas[1]
    return verbs


def get_list_of_adj(all_lemmas):
    adj = all_lemmas[2]
    return adj


#Count n most common words.
def count_words(words, n):
    print(Counter(words).most_common(n))