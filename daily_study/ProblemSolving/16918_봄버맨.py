# 23:30 start

from sys import stdin
input = stdin.readline
from collections import deque

R, C, N = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
print(R, C, N)
for b in board:
    print(b)