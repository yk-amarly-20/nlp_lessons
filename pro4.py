import nltk
import re

raw = """DENNIS: Listen, strange women lying in ponds distributing swords
is no basis for a system of goverment. Supreme executive power derives from 
a mandate from the masses, not from some farcical aquatic ceremony. """
tokens = nltk.word_tokenize(raw)

"""
# ステム:　接辞の除去
porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()
list1 = [porter.stem(t) for t in tokens]
print(list1)
list2 = [lancaster.stem(t) for t in tokens]
print(list2)
"""

"""
#　見出し語化
wnl = nltk.WordNetLemmatizer()
list3 = [wnl.lemmatize(t) for t in tokens]
print(list3)
"""


# raw2 = """ 'when I'M a Duchess,' she said to herself, (not in a very hopeful
# tone though), 'I won't have any pepper in my kitchen AT ALL. Soup does very
# well without - -Maybe it 's always pepper that makes people hot-tempered,'... """


# print(re.split(r' ', raw2)) => 改行文字を含んだまま
# print(re.split(r'[ \t\n]+', raw2))

# print(re.split(r'\W+', raw2))
