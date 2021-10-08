from collections import Counter
import re
def top_3_words(text):
    c = re.compile(r'[A-Za-z\']+')

    text = c.findall(text)
    counter = Counter(sorted(text))
    c = []
    for i, j in counter.most_common(3):
        c.append(i.lower())
    if not any(map(str.isalpha, c)):
        return []
    return c

a = 'e e e e \'\'\' ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e'



