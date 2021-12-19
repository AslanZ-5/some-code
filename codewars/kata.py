def perimeter_sequence(a, n):
    # your code here
    return (a * n +(a*n)) * 2


def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i