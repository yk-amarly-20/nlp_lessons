from nltk.corpus import gutenberg
import nltk

alice = gutenberg.words('carroll-alice.txt')
print(len(set(alice)))
vocab = nltk.FreqDist(alice)
v100 = list(vocab)[:100]
mapping = nltk.defaultdict(lambda: 'UNK')
for v in v100:
    mapping[v] = v
alice2 = [mapping[v] for v in alice]
print(alice2[:100])
