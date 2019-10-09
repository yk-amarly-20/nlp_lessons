# 自動タグ付け（タガー）
from nltk.corpus import brown
import nltk

brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')

tags = [tag for (word, tag) in brown.tagged_words(categories='news')]
tag_fd = nltk.FreqDist(tags)
# print(tag_fd.max())

"""
# デフォルトタガ
# 全ての単語に同じ品詞を付与
raw = "I do not like green eggs and ham, I do not like them Sam I am!"
tokens = nltk.word_tokenize(raw)
default_tagger = nltk.DefaultTagger('NN')
print(default_tagger.tag(tokens))
"""


"""
# 正規表現タガー
# 正規表現で品詞を指定
patterns = [
    (r'.*ing$', 'VBG'),  # 動名詞
    (r'.*ed$', 'VBD'),  # 過去形
    (r'.*es$', 'VBZ'),  # 三人称単数形
    (r'.*ould$', 'MD'),  # 法助動詞
    (r'.*\'s$', 'NN$'),  # 名詞の所有格
    (r'.*s$', 'NNS'),  # 名詞の複数形
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # 基数
    (r'.*', 'NN')   # 名詞
]

regexp_tagger = nltk.RegexpTagger(patterns)
# print(regexp_tagger.tag(brown_sents[3]))
print(regexp_tagger.evaluate(brown_tagged_sents))
"""

# ルックアップタガー

