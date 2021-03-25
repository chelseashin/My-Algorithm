from sys import stdin
input = stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

N = int(input())
A = []
doors = []
for i in range(N):
    A.append(list(input().strip()))
    for j in range(N):
        if A[i][j] == "#":
            doors.append((i, j))
(sr, sc), (gr, gc) = doors
for a in A:
    print(a)

print((sr, sc), (gr, gc))