import sys
sys.stdin = open("14502_input.txt")
input = sys.stdin.readline
from itertools import combinations
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 바이러스 퍼트리기
def bfs():
    global MAX
    # 상태 복사할 때 꼭 for문으로 가져와 저장하기!
    lab = [x[:] for x in A]
    Q = deque([(r, c) for r, c in virus])
    virusCnt = 3
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < N and 0 <= nc < M) or lab[nr][nc]:
                continue
            lab[nr][nc] = 2
            Q.append((nr, nc))
            virusCnt += 1
    MAX = max(MAX, spaceCnt - virusCnt)
    return

N, M = map(int, input().split())
A = []
virus = []     # 초기 바이러스 위치
spaceCnt = 0       # 빈 공간
spaces = []
for i in range(N):
    A.append(list(map(int, input().split())))
    for j in range(M):
        if A[i][j] == 0:
            spaceCnt += 1
            spaces.append((i, j))
        elif A[i][j] == 2:
            virus.append((i, j))
MAX = 0
for comb in combinations(spaces, 3):    # 조합으로 벽 3개 세우기
    for r, c in comb:
        A[r][c] = 3
    bfs()
    for r, c in comb:
        A[r][c] = 0
print(MAX)