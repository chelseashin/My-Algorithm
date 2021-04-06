# 70% 시간초과
# Union-Find 써야 함..!

from sys import stdin
input = stdin.readline
from collections import deque

dr = (-1, 1, 0, 0, -1, 1, 1, -1)
dc = (0, 0, -1, 1, 1, 1, -1, -1)

def bfs():
    check = [[1] * C for _ in range(R)]
    while Q:
        n, r, c = Q.popleft()
        minN = n
        minR, minC = -1, -1
        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            if board[nr][nc] < minN:
                minN = board[nr][nc]
                minR, minC = nr, nc
        if (minR, minC) == (-1, -1):    # 갱신 X
            continue
        # print(n, (r, c), "=>", minN, (minR, minC))
        check[r][c] -= 1
        check[minR][minC] += 1
        Q.append((minN, minR, minC))
        # break
    for row in check:
        print(*row)
    
# main
R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
Q = deque()
for r in range(R):
    for c in range(C):
        Q.append((board[r][c], r, c))
# print(Q)
# for row in board:
#     print(row)
# print()
bfs()
