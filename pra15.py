# アナグラム抽出
from collections import defaultdict
from nltk.corpus import words

words = words.words('en')
anagrams = defaultdict(list)
for word in words:
    key = ''.join(sorted(word))
    anagrams[key].append(word)

print(anagrams['aeilnrt'])
