import nltk
from nltk.corpus import brown


if __name__ == "__main__":
    """
      text = nltk.word_tokenize('And now for something completely different')
      tag = nltk.pos_tag(text)
      print(tag)
    """

    """
    text = nltk.Text(w.lower() for w in nltk.corpus.brown.words())
    print(text.similar('woman'))
    """

    """
    news_tag = brown.tagged_words(categories='news')
    # tag_fd = nltk.FreqDist(tag for (word, tag) in news_tag)
    # print(tag_fd.keys())

    word_tag_pairs = nltk.bigrams(news_tag)
    list1 = list(nltk.FreqDist(a[1]
                               for (a, b) in word_tag_pairs if b[1] == 'NN'))
    print(list1)
    """

    wsj = nltk.corpus.treebank.tagged_words(tagset='universal')
    word_tag_fd = nltk.FreqDist(wsj)
    print([word + "/" + tag for (word, tag) in word_tag_fd if tag.startswith('V')])
