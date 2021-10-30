import re


def count_smileys(arr):
    arr = ' '.join(arr)
    a = re.compile(r'([:|;][-|~]?[\)|D])')
    c = a.findall(arr)
    return len(c)
