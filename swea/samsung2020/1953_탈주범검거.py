import sys
sys.stdin = open('1953_input.txt')
from collections import deque

# 상하좌우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

rev = (1, 0, 3, 2)

# 터널 구조물 모양
tunnel = [[],
          [1, 1, 1, 1],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [1, 0, 0, 1],
          [0, 1, 0, 1],
          [0, 1, 1, 0],
          [1, 0, 1, 0]]

def bfs(sr, sc):
    visited = [[0] * M for _ in range(N)]
    visited[sr][sc] = 1
    Q = deque([(sr, sc)])
    ans = 1
    time = 1
    while Q:
        if time == L:
            break
        qlen = len(Q)
        for _ in range(qlen):
            r, c = Q.popleft()
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if not (0 <= nr < N and 0 <= nc < M):
                    continue
                if not A[nr][nc]:
                    continue
                if visited[nr][nc]:
                    continue
                if tunnel[A[r][c]][d] and tunnel[A[nr][nc]][rev[d]]:
                    visited[nr][nc] = 1
                    Q.append((nr, nc))
                    ans += 1
        time += 1
    return ans

# main
T = int(input())
for tc in range(T):
    N, M, R, C, L = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    print("#{} {}".format(tc+1, bfs(R, C)))

    # 1 5
    # 2 15
    # 3 29
    # 4 67
    # 5 71