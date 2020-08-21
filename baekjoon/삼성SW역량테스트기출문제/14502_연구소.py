import sys
sys.stdin = open('14502_input.txt')

from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs():
    visited = [[0] * M for _ in range(N)]
    q = deque()
    for r, c in virus:
        q.append((r, c))
        visited[r][c] = 1
    # print(q)
    # print(visited)
    temp = 0
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if A[nr][nc] or visited[nr][nc]:
                continue
            visited[nr][nc] = 1
            temp += 1
            q.append((nr, nc))
    # print(temp)
    return space - temp

# main
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
MAX = float('-inf')

virus = deque()
space = -3
for i in range(N):
    for j in range(M):
        if A[i][j] == 0:
            space += 1
        if A[i][j] == 2:
            virus.append((i, j))
# print(space)
# print(virus)

for ir in range(N):
    for ic in range(M):
        for jr in range(N):
            for jc in range(M):
                if (ir == jr and ic == jc):
                    continue
                for kr in range(N):
                    for kc in range(M):
                        if (kr == ir and kc == ic) or (kr == jr and kc == ic):
                            continue
                        if (A[ir][ic] or A[jr][jc] or A[kr][kc]):
                            continue
                        A[ir][ic], A[jr][jc], A[kr][kc] = 1, 1, 1
                        MAX = max(MAX, bfs())
                        A[ir][ic], A[jr][jc], A[kr][kc] = 0, 0, 0
print(MAX)