import sys
sys.stdin = open('2583_input.txt')

from collections import deque
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs(sr, sc):
    global M, N, A, temp
    Q = deque([(sr, sc)])
    temp += 1
    A[sr][sc] = 0
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < M and 0 <= nc < N):
                continue
            if not A[nr][nc]:
                continue
            temp += 1
            A[nr][nc] = 0
            Q.append((nr, nc))

M, N, K = map(int, input().split())
A = [[1] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for r in range(y1, y2):
        for c in range(x1, x2):
            A[r][c] = 0
cnt = 0
C = []
for i in range(M):
    for j in range(N):
        temp = 0
        if A[i][j]:
            bfs(i, j)
            cnt += 1
            C.append(temp)
# print(A)
print(cnt)
print(*sorted(C))