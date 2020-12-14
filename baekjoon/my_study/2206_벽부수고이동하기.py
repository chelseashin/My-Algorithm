import sys
sys.stdin = open("2206_input.txt")
input = sys.stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs():
    Q = deque([(0, 0, 1)])
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1
    visited[0][0][1] = 1

    while Q:
        r, c, b = Q.popleft()
        # 종료조건
        if r == N-1 and c == M-1:
            return visited[r][c][b]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            # 벽이 아닌 경우 일반적인 bfs
            if not A[nr][nc] and not visited[nr][nc][b]:
                visited[nr][nc][b] = visited[r][c][b] + 1
                Q.append((nr, nc, b))
            # 벽 뚫을 기회 남았다면
            if A[nr][nc] and b == 1:
                visited[nr][nc][0] = visited[r][c][b] + 1
                Q.append((nr, nc, 0))
        # print(Q)
        # for v in visited:
        #     print(v)
        # print()
    return -1

# main
N, M = map(int, input().split())
A = [list(map(int, input().strip())) for _ in range(N)]
# for a in A:
#     print(a)

print(bfs())