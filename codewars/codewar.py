import re
import functools
from collections import deque


def count_smileys(arr):
    arr = ' '.join(arr)
    a = re.compile(r'([:|;][-|~]?[\)|D])')
    c = a.findall(arr)
    return len(c)


def number(lines):
    return [f'{i + 1}: {lines[i]}' for i in range(0, len(lines))]


def isequal(a, b):
    return all([True if type(a[i]) == type(b[i]) else False for i in range(len(a))])


def greet(name):
    return f"Hello, {name} how are you doing today?"


def solve(s):
    a = re.compile(r'[aiueo]+')
    return max(map(len, a.findall(s)))


def solve(s):
    b = [1 if i.islower() else 0 for i in s]
    if sum(b) >= len(s) // 2:
        return s.lower()
    else:
        return s.upper()


def run_length_encoding(s):
    if s:
        x = []
        x.append(s[0])
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                x[-1] += s[i]
            else:
                x.append(s[i])
        return [[len(i), i[0]] for i in x]
    return []


def run_length_encoding2(s):
    from itertools import groupby
    return [[len(list(b)), i] for i, b in groupby(s)]


def persistence(n):
    count = 0
    while len(str(n)) != 1:
        count += 1
        c = list(map(int, str(n)))
        n = functools.reduce(lambda a, b: a * b, c)

    return count


def count_nines(n):
    return ''.join(list(map(str, range(1, n + 1)))).count('9')


# dir = 'cc'
# c = deque()
# for i in a:
#     i.reverse()
# a.reverse()
# print(a)

#
r =  [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
t = [list(reversed(i)) for i in zip(*r)]
print(t)


a = [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]


def rotate(matrix, direction):
    if direction == "counter-clockwise":
        a = [list(i) for i in zip(*matrix)]
        a.reverse()
        return a
    if direction == "clockwise":
        return [list(reversed(i)) for i in zip(*r)]

