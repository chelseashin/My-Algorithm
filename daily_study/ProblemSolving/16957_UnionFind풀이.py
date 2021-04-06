# https://www.acmicpc.net/source/20088005
# 시간 1위
# Union-Find 알고리즘 사용

from sys import stdin
input = stdin.readline

dr = (0, -1, 1, 0, 0, -1, 1, 1, -1)
dc = (0, 0, 0, -1, 1, 1, 1, -1, -1)

def findParent(s):
    if A[s] == s:
        return s
    else:
        A[s] = findParent(A[s])
        return A[s]

# main
R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
A = [i for i in range(R*C)]
for sr in range(R):
    for sc in range(C):
        r, c = sr, sc
        for d in range(9):
            nr = sr + dr[d]
            nc = sc + dc[d]
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            if board[nr][nc] < board[r][c]:
                r, c = nr, nc
        A[sr*C+sc] = r*C + c
# print(A)

check = [[0] * C for _ in range(R)]
for r in range(R):
    for c in range(C):
        root = findParent(r*C+c)
        check[root//C][root%C] += 1

for row in check:
    print(*row)