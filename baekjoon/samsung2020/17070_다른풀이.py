import sys
sys.stdin = open('17070_input.txt')
input = sys.stdin.readline

# 다이나믹 프로그래밍

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
d = [[[0]*3 for _ in range(n)] for _ in range(n)]

d[0][1][0] = 1

for i in range(n):
    for j in range(1,n):
        if a[i][j] == 1:
            continue
        if j-1 >= 0:
            d[i][j][0] += d[i][j-1][0]
            d[i][j][0] += d[i][j-1][1]

        if i-1 >= 0 and j-1 >= 0 and a[i-1][j] == 0 and a[i][j-1] == 0:
            d[i][j][1] += d[i-1][j-1][0]
            d[i][j][1] += d[i-1][j-1][1]
            d[i][j][1] += d[i-1][j-1][2]

        if i-1 >= 0:
            d[i][j][2] += d[i-1][j][1]
            d[i][j][2] += d[i-1][j][2]
# print(d)
print(sum(d[n-1][n-1]))