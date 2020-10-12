import sys
sys.stdin = open('14502_input.txt')
input = sys.stdin.readline
from collections import deque
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs():
    global MAX
    lab = [a[:] for a in A]
    q = deque([(r, c) for r, c in virus])
    temp = 0
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if lab[nr][nc] == 0:
                lab[nr][nc] = 2
                temp += 1
                q.append((nr, nc))
    MAX = max(MAX, space-temp)
    return

def dfs(depth):
    if depth == 3:
        bfs()
        return
    for r in range(N):
        for c in range(M):
            if A[r][c]:
                continue
            A[r][c] = 3     # 새로운 벽 세우기
            dfs(depth+1)
            A[r][c] = 0

N, M = map(int, input().split())
A = []
virus = []
space = -3
for i in range(N):
    row = list(map(int, input().split()))
    A.append(row)
    for j in range(M):
        if A[i][j] == 0:
            space += 1
        if A[i][j] == 2:
            virus.append((i, j))

MAX = float('-inf')
dfs(0)
print(MAX)