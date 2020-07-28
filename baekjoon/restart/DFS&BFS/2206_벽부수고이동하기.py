import sys
sys.stdin = open('2206_input.txt')
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs(sr, sc):
    global A, visited, MIN, N, M
    # 행, 열, 폭탄의 수
    Q.append((sr, sc, 1))
    visited[0][sr][sc] = 1
    visited[1][sr][sc] = 1
    while Q:
        r, c, bomb = Q.popleft()
        if r == N-1 and c == M-1:
            MIN = visited[bomb][r][c]
            return
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            # 폭탄 기회 있을 때
            if A[nr][nc] == 1 and bomb == 1:
                if visited[0][nr][nc]:
                    continue
                visited[0][nr][nc] = visited[1][r][c] + 1
                Q.append((nr, nc, 0))
            # 폭탄 기회 없을 때
            elif A[nr][nc] == 0 and visited[bomb][nr][nc] == 0:
                visited[bomb][nr][nc] = visited[bomb][r][c] + 1
                Q.append((nr, nc, bomb))

N, M = map(int, input().split())
A = [list(map(int, input())) for _ in range(N)]
# 기회 사용했을 때, 사용하지 않았을 때의 차이를 구분하기 위해 2개 만들기
visited = [[[0] * M for _ in range(N)] for _ in range(2)]

MIN = float('inf')
Q = deque()
bfs(0, 0)
# print(visited)
if MIN == float('inf'):
    MIN = -1
print(MIN)