# 12:00 start

dr = (0, -1, 0, 1)
dc = (1, 0, -1, 0)

import sys
input = sys.stdin.readline


N = int(input())
A = [[0] * 101 for _ in range(101)]
for _ in range(N):
    c, r, d, g = map(int, input().split())
    curve = [d]             # 방향 담는 리스트
    for i in range(g):      # 세대별로 이동
        clen = len(curve)
        for j in range(clen-1, -1, -1):     # 커브
            curve.append((curve[j]+1) % 4)
    A[r][c] = 1
    for dd in curve:
        r += dr[dd]
        c += dc[dd]
        A[r][c] = 1
for a in A:
    print(a)

square = 0
for i in range(100):
    for j in range(100):
        if A[i][j] and A[i][j+1] and A[i+1][j] and A[i+1][j+1]:
            square += 1
print(square)