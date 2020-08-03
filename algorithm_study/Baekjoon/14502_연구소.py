import sys
sys.stdin = open('14502_input.txt')

# 나의 코드 - 메모리, 시간 최적화
from collections import deque
import copy

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs():
    global q, A, MAX
    Q = deque()
    Q.extend(q)
    C = copy.deepcopy(A)
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

    safeArea = 0
    for i in range(N):
        for j in range(M):
            if C[i][j] == 0:
                safeArea += 1
    if MAX < safeArea:
        MAX = safeArea


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

q = deque()
for i in range(N):
    for j in range(M):
        if A[i][j] == 2:
            q.append((i, j))
dfs(0)
print(MAX)


# 성공
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
# ans = 0
# 
# def bfs():
#     global ans
#     w = copy.deepcopy(a)
#     for i in range(n):
#         for j in range(m):
#             if w[i][j] == 2:
#                 q.append([i, j])
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < m:
#                 if w[nx][ny] == 0:
#                     w[nx][ny] = 2
#                     q.append([nx, ny])
# 
#     cnt = 0
#     for i in w:
#         cnt += i.count(0)
#     ans = max(ans, cnt)
# 
# def wall(x):
#     if x == 3:
#         bfs()
#         return
#     for i in range(n):
#         for j in range(m):
#             if a[i][j] == 0:
#                 a[i][j] = 1
#                 wall(x+1)
#                 a[i][j] = 0
# 
# n, m = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(n)]
# q = deque()
# wall(0)
# print(ans)