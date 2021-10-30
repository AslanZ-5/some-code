import re


def count_smileys(arr):
    arr = ' '.join(arr)
    a = re.compile(r'([:|;][-|~]?[\)|D])')
    c = a.findall(arr)
    return len(c)

def number(lines):
    return [f'{i+1}: {lines[i]}' for i in range(0,len(lines))]