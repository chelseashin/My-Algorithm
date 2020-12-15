import sys
sys.stdin = open("14502_input.txt")
input = sys.stdin.readline

from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 바이러스 퍼트리기
def bfs():
    global MAX
    # 상태 복사할 때 꼭 for문으로 가져와 저장하기!
    lab = [x[:] for x in A]
    Q = deque([(r, c) for r, c in virus])

    virusCnt = 0
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < M) or lab[nr][nc]:
                continue
            lab[nr][nc] = 2
            Q.append((nr, nc))
            virusCnt += 1
    MAX = max(MAX, safeArea - virusCnt)
    return

# 벽 세우기
def dfs(depth):
    if depth == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if A[i][j]:
                continue
            A[i][j] = 3
            dfs(depth+1)
            A[i][j] = 0

# main
N, M = map(int, input().split())
A = []
MAX = float('-inf')
safeArea = -3       # 빈 공간
virus = []     # 초기 바이러스 위치
for i in range(N):
    A.append(list(map(int, input().split())))
    for j in range(M):
        if A[i][j] == 0:
            safeArea += 1
        elif A[i][j] == 2:
            virus.append((i, j))

# 방법 1. DFS로 벽 세우기
# 129760KB,	1392ms
dfs(0)

# 방법 2. 6중 for문으로 0인 공간에 한 번에 벽 세우기
# 133032KB,	1352ms
# for ir in range(N):
#     for ic in range(M):
#         if A[ir][ic]:
#             continue
#         for jr in range(N):
#             for jc in range(M):
#                 if A[jr][jc]:
#                     continue
#                 if (ir == jr and ic == jc):
#                     continue
#                 for kr in range(N):
#                     for kc in range(M):
#                         if A[kr][kc]:
#                             continue
#                         if (kr == ir and kc == ic) or (kr == jr and kc == jc):
#                             continue
#                         A[ir][ic], A[jr][jc], A[kr][kc] = 1, 1, 1
#                         bfs()
#                         A[ir][ic], A[jr][jc], A[kr][kc] = 0, 0, 0
print(MAX)