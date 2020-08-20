import sys
sys.stdin = open('17141_input.txt')

from collections import deque
from itertools import combinations

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs(Q):
    temp = 0
    visited = [[-1] * N for _ in range(N)]
    for pos in Q:
        r, c = pos
        visited[r][c] = 0
        temp += 1
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if lab[nr][nc] == 1 or visited[nr][nc] > -1:
                continue
            visited[nr][nc] = visited[r][c] + 1
            Q.append((nr, nc))
            temp += 1
    if temp == space:
        return visited[r][c]
    return float('inf')

# main
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
min_time = float('inf')

space = 0
virus_cnt = 0
virus_pos = []
for i in range(N):
    for j in range(N):
        if lab[i][j] != 1:
            space += 1
        if lab[i][j] == 2:
            virus_cnt += 1
            virus_pos.append((i, j))

for comb in list(combinations(virus_pos, M)):
    Q = deque(comb)
    min_time = min(min_time, bfs(Q))
if min_time == float('inf'):
    print(-1)
else:
    print(min_time)