import nltk
from nltk.corpus import brown

brown_news_tagged = brown.tagged_words(categories='news')
tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
tag_fd.plot(cumulative=True)
