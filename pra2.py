
import nltk
from nltk.corpus import gutenberg
emma = gutenberg.words("austen-emma.txt")

"""
# 各ファイルの単語平均長、文平均長、各単語の出現回数を算出
for fileid in gutenberg.fileids():
    # 総文字数
    num_chars = len(gutenberg.raw(fileid))
    # 総単語数
    num_words = len(gutenberg.words(fileid))
    # 総文数
    num_sents = len(gutenberg.sents(fileid))
    # 異なり文字数
    num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
    print(int(num_chars / num_words), int(num_words / num_sents), int(num_words / num_vocab), fileid)
"""
"""
# 法助動詞の数をカウント
from nltk.corpus import brown
news_text = brown.words(categories='news')
fdist = nltk.FreqDist(news_text)
modals = ['can', 'could', 'may', 'might', 'will', 'must']
for m in modals:
    print('{0} : {1}'.format(m, fdist[m]))
"""

"""
# 法助動詞の数でジャンル予測
from nltk.corpus import brown
cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre)
)
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'will', 'must']
cfd.tabulate(conditions=genres, samples=modals)
"""

"""
# 就任演説コープス
from nltk.corpus import inaugural
cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ["america", "citizen"]
    if w.lower().startswith(target)
)
cfd.plot()
"""

"""
# 世界人権宣言
from nltk.corpus import udhr
languages = ['Chickasaw','English', 'German_Deutsch', 
            'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
cfd = nltk.ConditionalFreqDist(
    (lang, len(word))
    for lang in languages
    for word in udhr.words(lang + '-Latin1')
)
cfd.plot(cumulative=True)
"""

"""
from nltk.corpus import brown
days = ['Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
cfd = nltk.ConditionalFreqDist(
    (target, day)
    for target in ['news', 'romance']
    for fileid in brown.fileids(categories=target)
    for day in days
    if day in brown.words(fileid)
)
cfd.plot()
"""


"""
# 辞書作成
from nltk.corpus import swadesh
fr2en = swadesh.entries(['fr', 'en'])
translate = dict(fr2en)
# print(translate['chien'])
# print(translate['jeter'])

de2en = swadesh.entries(['de', 'en'])
es2en = swadesh.entries(['es', 'en'])
translate.update(dict(de2en))
translate.update(dict(es2en))
print(translate['Hund'])
print(translate['perro'])
"""


"""
from nltk.corpus import state_union
words = ['men', 'women', 'people']
union_words = [w.lower() for w in state_union.words()]
cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in state_union.fileids()
    for target in words
    for w in state_union.words(fileid)
    if w.lower() == target 
)
cfd.plot()
"""

"""
from nltk.corpus import names
cfd = nltk.ConditionalFreqDist(
    (fileid, name[0])
    for fileid in names.fileids()
    for name in names.words(fileid)
)
cfd.plot()
"""



