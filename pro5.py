from random import randint

# セグメントに従い、テキストを分割


def segment(text, segs):
    words = []
    last = 0
    for i in range(len(segs)):
        if segs[i] == '1':
            words.append(text[last:i + 1])
            last = i + 1
    words.append(text[last:])
    return words

# 目的関数を定義


def evaluate(text, segs):
    words = segment(text, segs)
    text_size = len(words)
    lexicon_size = len(' '.join(list(set(words))))
    return text_size + lexicon_size


def flip(segs, pos):
    return segs[:pos] + str(1 - int(segs[pos])) + segs[pos + 1:]


def flip_n(segs, n):
    for i in range(n):
        segs = flip(segs, randint(0, len(segs) - 1))
    return segs


def anneal(text, segs, iterations, cooling_rate):
    temperature = float(len(segs))
    while temperature > 0.5:
        best_segs, best = segs, evaluate(text, segs)
        for i in range(iterations):
            guess = flip_n(segs, int(round(temperature)))
            score = evaluate(text, guess)
            if score < best:
                best, best_segs = score, guess
        score, segs = best, best_segs
        temperature = temperature / cooling_rate
        print(evaluate(text, segs), segment(text, segs))
    return segs


if __name__ == "__main__":
    text = "doyouseethekittyseethedoggydoyoulikethekittylikethedoggy"
    seg1 = "0000000000000001000000000010000000000000000100000000000"
    anneal(text, seg1, 10000, 1.2)
