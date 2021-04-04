from sys import stdin
input = stdin.readline
from collections import deque
from heapq import heappush, heappop

R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
Q = deque()
for r in range(R):
    for c in range(C):
        Q.append((board[r][c], r, c))
print(Q)
for row in board:
    print(row)