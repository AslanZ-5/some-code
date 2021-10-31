import re


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
    return max(map(len,a.findall(s)))
