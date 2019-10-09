# ファイルからテキストを読み込む
import re
import nltk


def get_text(file):
    """ファイルからテキストを読み込み、空白文字を空白にして、HTMLマークアップを消去"""
    text = open(file).read()
    text = re.sub('\s+', ' ', text)
    text = re.sub('<.*?>', ' ', text)
    return text

# 入れ子になった辞書作成の関数


def insert(trie, key, value):
    if key:
        first, rest = key[0], key[1:]
        if first not in trie:
            trie[first] = {}
        insert(trie[first], rest, value)
    else:
        trie['value'] = value


if __name__ == "__main__":
    trie = nltk.defaultdict(dict)
    insert(trie, 'chat', 'cat')
    insert(trie, 'chien', 'dog')
    insert(trie, 'chair', 'flesh')
    insert(trie, 'chic', 'stylish')
    trie = dict(trie)
    print(trie)
