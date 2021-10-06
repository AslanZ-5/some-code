# import re
# c = 'big brown fox cought a bad rabbit'
# positive = 0
# negative = 0
# for i in c.split():
#     r = re.compile(r'^[a-m]').findall(i.lower())
#     if r:
#         positive += 1
#     else:
#         negative +=1
# if positive >= negative:
#     print(True)
# else:
#     print(False)


#
# d = 'Xylophones'
# tr = re.compile(r'^[a-m]').findall(i.lower())
# print(tr)

from itertools import product, permutations, combinations

count = 0
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    global count
    count += n
    return fib(n - 1) + fib(n - 2)

print(count)
print(fib(5))
