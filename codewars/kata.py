import itertools
def perimeter_sequence(a, n):
    # your code here
    return (a * n + (a * n)) * 2


def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i


def closest_num(arr, tar):
    low = 0
    high = len(arr) - 1
    closest = None
    min_dif = float('inf')

    while low <= high:
        mid = (low + high) // 2
        if mid + 1 < len(arr):
            right_n = abs(arr[mid + 1] - tar)
        if mid > 0:
            left_n = abs(arr[mid - 1] - tar)
        if min_dif > right_n:
            min_dif = right_n
            closest = arr[mid + 1]
        elif min_dif > left_n:
            min_dif = left_n
            closest = arr[mid - 1]

        if arr[mid] < tar:
            low = mid + 1
        elif arr[mid] > tar:
            high = mid - 1
        else:
            return arr[mid]
    return closest


# print(closest_num([2, 6, 7, 8, 8, 9], 4))
import timeit

start = timeit.timeit()


def peak(arr):
    pos = []
    peaks = []
    for i in range(len(arr)):
        if i - 1 > 0 and i + 1 < len(arr):
            if arr[i - 1] < arr[i] and arr[i + 1] < arr[i]:
                pos.append(i)
                peaks.append(arr[i])
    return {'pos': pos, 'peaks': peaks}


# print(peak([3,2,3,6,4,1,2,3,2,1,2,2,2,1]))

stop = timeit.timeit()
# print('time: ',start - stop)


str_int = "apples, pears # and bananas\ngrapes\nbananas !apples"
# str_int = "a #b\nc\nd $e f g"
mark = ["#", "!"]


# mark = ["#", "$"]
def solution(string, markers):
    t = []
    ls = string.split('\n')

    for i in ls:
        inx = []
        for j in markers:
            if j in i:
                inx.append(i.index(j))

        if inx:
            t.append(i[:min(inx)])
        else:
            t.append(i)
    return '\n'.join(map(str.rstrip, t))


def reverse_int(int_input):
    r = str(int_input)
    if r[0] == '-':
        r = r[1:]
        return int(r[::-1]) * -1
    return int(r[::-1])


def arg_words_len(w):
    for p in '!?,.:;':
        w = w.replace(p, '')
    words = w.split()
    avr = sum(len(word) for word in words) / len(words)
    return round(avr, 2)


def find_the_strongest_apes(_list):
    dc = {"Gorilla": None, "Gibbon": None, "Orangutan": None, "Chimpanzee": None}
    a = [(i['name'], (i['weight'] + i['height']), i['type']) for i in _list]
    a = sorted(a, key=lambda x: x[0].lower())
    a = sorted(a, key=lambda x: x[1], reverse=True)
    for i in a:
        if dc[i[2]] is None:
            dc[i[2]] = i[0]

    return dc


list1 = ([{"name": "aba", "weight": 100, "height": 120, "type": "Gorilla"},
         {"name": "abb", "weight": 100, "height": 120.01, "type": "Gorilla"},
         {"name": "abc", "weight": 100, "height": 100, "type": "Orangutan"},
         {"name": "abd", "weight": 100.01, "height": 100, "type": "Orangutan"}])

num = 1234567
remainder1 = num % 13
remainder2 = None
num = str(num)[::-1]
t = [1, 10, 9, 12, 3, 4]


a = "a lot of words for a single line"
c = 0
for i in range(len(a)):
    if c == 10 -1:
        a = a[:i] +'-' + a[i:]
        c = 0
    c += 1
print(a)

