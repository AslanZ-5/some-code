import re
import string


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


def solve(s):
    c = re.compile('[auieo]')
    s = c.split(s)
    return max([sum(map(lambda x: string.ascii_lowercase.index(x) + 1, i)) for i in s if i])


def spin_words(sentence):
    return ' '.join([i[::-1] if len(i) >= 5 else i for i in sentence.split()])


def filter_string(string):
    return int(''.join([i for i in string if i.isnumeric()]))


a = '1349876562bsdbcjksdc bsjdc11231231sc nsdj cs,c n'
c = re.compile(r'(?<=[13579])\d')


def benary_search(lst, tar):
    l = 0
    h = len(lst) - 1
    while l <= h:
        mid = (l + h) // 2
        if lst[mid] == tar:
            print(tar)
            return True
        elif lst[mid] < tar:
            l = mid +1
        else:
            h = mid -1
    return False

def benary_search_rec(lst,tar,l,h):
    if l > h:
        return False
    else:
        mid = (l + h) //2
        if lst[mid] == tar:
            print(tar)
            return True
        elif tar < lst[mid]:
            return benary_search_rec(lst,tar,l,mid-1)
        else:
            return benary_search_rec(lst,tar,mid+1, h)


def move_zeros(r):
    for i in r:
        if i == 0:
            r.remove(i)
            r.append(i)
    return r