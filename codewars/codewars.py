import re
import string
import math


def fold_array(array, runs):
    for i in range(runs):
        x = int((len(array) - 1) / 2)
        if len(array) % 2 != 0:
            b = array[:x]
        b = array[:x + 1]
        c = array[x + 1:]
        c.reverse()
        array = [b[i] + c[i] for i in range(len(b))]
        if len(array) % 2 != 0:
            array.append(array[x])
        return array


def digital_root(n):
    x = True
    while x:
        n = sum(list(map(int, str(n))))
        if len(str(n)) == 1:
            x = False

    return n


def solve(st):
    st = sorted(st)
    c = []
    for i in range(1, len(st)):
        if ord(st[i]) == ord(st[i - 1]):
            c.append(False)
        elif ord(st[i]) == ord(st[i - 1]) + 1:
            c.append(True)
        else:
            c.append(False)
    return all(c)


def array_plus(array1, array2):
    return sum(array1 + array2)


# r = [1, 512, 4913, 5832, 17576, 19683]
#
# for i in r:
#     print(round(i ** (1. / 3.)) != sum(map(int, str(i))))
#     if round(i ** (1. / 3.)) != sum(map(int, str(i))):
#         r.remove(i)
# print(r)

# Consonant value
def solve(s):
    c = re.compile('[auieo]')
    s = c.split(s)
    return max([sum(map(lambda x: string.ascii_lowercase.index(x) + 1, i)) for i in s if i])


def spin_words(sentence):
    return ' '.join([ i[::-1] if len(i) >= 5 else i for i in sentence.split() ])


def filter_string(string):
    return int(''.join([i for i in string if i.isnumeric()]))

a = '1349876562bsdbcjksdc bsjdc11231231sc nsdj cs,c n'
c = re.compile(r'(?<=[13579])\d')
print(c.findall(a))




