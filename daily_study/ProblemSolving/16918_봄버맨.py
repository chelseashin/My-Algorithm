# 23:30 start
# 24:10 9%에서 틀렸습니다..

from sys import stdin
input = stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bomberman():
    check = [["0" for _ in range(C)] for _ in range(R)]
    for sr in range(R):
        for sc in range(C):
            if board[sr][sc] == "O":
                check[sr][sc] = "."
                # BFS
                for d in range(4):
                    nr = sr + dr[d]
                    nc = sc + dc[d]
                    if not (0 <= nr < R and 0 <= nc < C):
                        continue
                    check[nr][nc] = "."
    for i in range(R):
        for j in range(C):
            print(check[i][j], end="")
        print()

# main
R, C, N = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
# print(R, C, N)
# for b in board:
#     print(b)
# print()

if not N % 2:
    for _ in range(R):
        print("O" * C)

elif N % 4 == 1:
    for i in range(R):
        for j in range(C):
            print(board[i][j], end="")
        print()

elif N % 4 == 3:
    bomberman()
