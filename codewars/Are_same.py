a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
x = set(map(lambda x: pow(x,2),a))
print(bool(set(b).intersection(x)))



b = [2]

print()

