from nltk.corpus import brown


def search1(substring, words):
    for word in words:
        if substring in word:
            yield word


if __name__ == "__main__":
    words = brown.words()
    for item in search1('zz', words):
        print(item)
