import sys
sys.stdin = open('14502_input.txt')

# 나의 코드 - 메모리, 시간 최적화
from collections import deque
from copy import deepcopy

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 바이러스 퍼트리기
def bfs():
    global q, A, MAX
    Q = deque()
    Q.extend(q)
    C = deepcopy(A)
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if C[nr][nc] == 0:
                C[nr][nc] = 2
                Q.append((nr, nc))
    # 최대 안전영역 찾기
    safeArea = 0
    for i in range(N):
        for j in range(M):
            if C[i][j] == 0:
                safeArea += 1
    if MAX < safeArea:
        MAX = safeArea

# 벽 3개 세울 수 있는 모든 경우의 수
def dfs(depth):
    if depth == 3:
        bfs()
        # print(A)
        return
    for i in range(N):
        for j in range(M):
            if A[i][j] == 0:
                A[i][j] = 1
                dfs(depth + 1)
                A[i][j] = 0

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
MAX = 0

# 미리 바이러스 있는 위치 q에 담기
q = deque()
for i in range(N):
    for j in range(M):
        if A[i][j] == 2:
            q.append((i, j))
dfs(0)
print(MAX)