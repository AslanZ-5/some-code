from itertools import permutations, combinations


def choose_best_sum(t, k, ls):
    c = 0
    for i in combinations(ls, k):
        if sum(i) <= t:
            if t - sum(i) < t - c:
                c = sum(i)
    if c:
        return c
    return None


t = 230  # maximum sum of distances
k = 4  # number of towns to visit
ls = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]  # list of distance
print(choose_best_sum(t, k, ls))
# print(list(combinations(ls,k)))
# c = []
# for i in combinations(ls,k):
#     if sum(i)<= t:
#         c = list(i)
#         print(sum(c),c)
#         if t - sum(i) < sum(c):
#             c = list(i)
# print(c)
