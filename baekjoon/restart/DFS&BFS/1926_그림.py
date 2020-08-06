import sys
sys.stdin = open('1926_input.txt')

from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs(sr, sc):
    global N, M, A, MAX
    Q = deque([(sr, sc)])
    A[sr][sc] = 0
    temp = 0
    while Q:
        r, c = Q.popleft()
        temp += 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if A[nr][nc] == 0:
                continue
            A[nr][nc] = 0
            Q.append((nr, nc))
    if temp > MAX:
        MAX = temp

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
MAX = float('-inf')
for i in range(N):
    for j in range(M):
        if A[i][j]:
            bfs(i, j)
            cnt += 1
# print(A)
if cnt:
    print(cnt)
    print(MAX)
else:
    print(cnt)
    print(0)