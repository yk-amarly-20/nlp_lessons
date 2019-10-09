import nltk
from urllib.request import urlopen
import re
url = 'https://edition.cnn.com/2019/09/21/asia/north-korean-defector-funeral-intl-hnk/index.html'
html = urlopen(url).read()
html = html.decode()
"""
print(type(html))
print(len(raw))
print(raw[:75])
"""


def clean_html(html):
    """
    Copied from NLTK package.
    Remove HTML markup from the given string.

    :param html: the HTML string to be cleaned
    :type html: str
    :rtype: str
    """
    # First we remove inline JavaScript/CSS:
    cleaned = re.sub(r"(?is)<(script|style).*?>.*?()", "", html.strip())
    # Then we remove html comments. This has to be done before removing regular
    # tags since comments can contain '>' characters.
    cleaned = re.sub(r"(?s)[\n]?", "", cleaned)
    # Next we can remove the remaining tags:
    cleaned = re.sub(r"(?s)<.*?>", " ", cleaned)
    # Finally, we deal with whitespace
    cleaned = re.sub(r" ", " ", cleaned)
    cleaned = re.sub(r"  ", " ", cleaned)
    cleaned = re.sub(r"  ", " ", cleaned)
    return cleaned.strip()


raw = clean_html(html)
tokens = nltk.word_tokenize(raw)
