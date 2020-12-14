import sys
sys.stdin = open("2206_input.txt")
input = sys.stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs():
    global MIN
    Q = deque([(0, 0, 1)])

    # 기회 사용했을 때, 사용하지 않았을 때의 차이를 구분하기 위해 2개 만들기
    visited = [[[0] * M for _ in range(N)] for _ in range(2)]
    visited[0][0][0] = 1
    visited[1][0][0] = 1
    while Q:
        r, c, b = Q.popleft()
        # 종료조건
        if r == N-1 and c == M-1:
            MIN = min(MIN, visited[b][r][c])
            return
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            # 폭탄 기회 남았다면
            if A[nr][nc] and b == 1:
                visited[0][nr][nc] = visited[1][r][c] + 1
                Q.append((nr, nc, 0))
            # 폭탄 기회 없고 벽이 아닌 경우 일반적인 bfs
            if not A[nr][nc] and not visited[b][nr][nc]:
                visited[b][nr][nc] = visited[b][r][c] + 1
                Q.append((nr, nc, b))

# main
N, M = map(int, input().split())
A = [list(map(int, input().strip())) for _ in range(N)]
# for a in A:
#     print(a)
MIN = float('inf')
bfs()
if MIN == float('inf'):
    print(-1)
else:
    print(MIN)