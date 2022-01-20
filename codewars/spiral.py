n = 10
a = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == 0:
            a[i][j] = 1
        if i == n -1 or j == n-1:
            a[i][j] = 1
        if j==0 and i > 1 :
            a[i][j] = 1



for i in a:
    print(i,end='\n')