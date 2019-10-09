from collections import defaultdict
from nltk.corpus import brown

counts = defaultdict(int)
tagged_text = brown.tagged_words(categories='news')
for (word, tag) in tagged_text:
    counts[tag] += 1

print(list(counts))
