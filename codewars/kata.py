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
a = [2, 6, 7, 8, 8, 9]
print(closest_num(a,4))