import nltk
from nltk.corpus import stopwords
#nltk.download()

from nltk.book import *
from nltk import word_tokenize
# print(text1)

# 引数の文字が使われている全ての場所をその周辺の場所とともに表示してくれる
# text1.concordance("monstrous")

# similarは引数の単語と同じ文脈で用いられている単語を探す
# text1.similar("monstrous")

# 共通の文脈で使われている単語を探す
# text2.common_contexts(["monstrous", "very"])

# 単語が使われている回数、位置をプロット
# text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

# 文字数
# print(len(text3))

# 重複込みの文字数
# print(len(set(text3)))

# ’a’が文章中で何回使われているのか
# num = 100 * text4.count('a') / len(text4)
# print(num)


# 'lol'が何回使われているのか
# num = 100 * text5.count('lol') / len(text5)
# print(num)


# 文章中で平均して同じ単語が何回使われているか
def lexical_diversity(text):
    return len(text) / len(set(text))

# 指定された単語が文章中で何パーセントを占めているか
def percentage(text, word):
    return 100 * text.count(word) / len(text)


# 文章をトークンに分割
fdist = FreqDist(text1)
# print(fdist["whale"])

# fdist.plot(50, cumulative=True)

# 長い単語が文章の内容を表すと考える
# V = set(text1)
# long_words = [w for w in V if len(w) > 15]
# print(long_words)

# fdist5 = FreqDist(text5)
#list = [w for w in set(text5) if len(w) > 7 and fdist5[w] > 7]
# print(list)

# コロケーション（よくあらわれる単語の組み合わせ）
# text4.collocations()

# 長さの分布の計算
# fdist = FreqDist([len(w) for w in text1])
# print(fdist.items())


# 語彙リストコーパス
# 一般的でない語やスペルミスをチェック
# def unusual_words(text):
#     text_vocab = set(w.lower() for w in text if w.isalpha())
#     english_vocab = set(w.lower() for w in nltk.corpus.words.words())
#     unusual = text_vocab.difference(english_vocab)
#     return sorted(unusual)

# print(unusual_words(text)


# ストップワードの除去　
# def content_fraction(text):
#     stop = stopwords.words('english')
#     content = [w for w in text if w.lower() not in stop]
#     return len(content) / len(text)

# print(content_fraction(text1))


# ターゲットパズル
# puzzule_letters = nltk.FreqDist('egivrvonl')
# obligatory = 'r'
# wordlist = nltk.corpus.words.words()
# ans = [w for w in wordlist if len(w) > 6 
#                             and obligatory in w
#                             and nltk.FreqDist(w) <= puzzule_letters]
# print(ans)


# 名前コープス
names = nltk.corpus.names
# male_names = names.words('male.txt')
# female_names = names.words('female.txt')
# both_names = [w for w in male_names if w in female_names]
# print(both_names)


# cfd = nltk.ConditionalFreqDist(
#     (fileid, name[-1])
#     for fileid in names.fileids()
#     for name in names.words(fileid)
# )
# cfd.plot()

# nltk.chat.chatbots()






