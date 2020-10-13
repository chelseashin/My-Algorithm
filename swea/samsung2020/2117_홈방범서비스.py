import sys
sys.stdin = open('2117_input.txt')
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

KLst = [K * K + (K-1) * (K-1) for K in range(25)]

# 시작점에서 K 크기 만큼
def bfs(sr, sc):
    global MAX
    visited = [[0] * N for _ in range(N)]
    visited[sr][sc] = 1
    Q = deque([(sr, sc)])
    home = 0     # 서비스 받는 집의 수
    # 서비스 영역의 크기 k 결정
    for k in range(1, N+2):
        qlen = len(Q)
        for _ in range(qlen):   # 새로 들어오는 좌표들과 구분
            r, c = Q.popleft()
            if A[r][c]:
                home += 1
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                if visited[nr][nc]:
                    continue
                visited[nr][nc] = 1
                Q.append((nr, nc))
        if home * M >= KLst[k]:
            MAX = max(MAX, home)

# main
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    MAX = float('-inf')

    for i in range(N):
        for j in range(N):
            bfs(i, j)

    print("#{} {}".format(tc+1, MAX))
    # 1 5
    # 2 4
    # 3 24
    # 4 48
    # 5 3
    # 6 65
    # 7 22
    # 8 22
    # 9 78
    # 10 400