from nltk.corpus import words
from collections import defaultdict

last_letters = defaultdict(list)
words = words.words('en')
for word in words:
    key = word[-2:]
    last_letters[key].append(word)

print(last_letters['ly'])
