import sys
sys.stdin = open('5188_input.txt')

from collections import deque
dr = (0, 1)
dc = (1, 0)

def bfs(sr, sc):
    global N, A, V
    Q = deque([(sr, sc)])
    while Q:
        r, c = Q.popleft()
        for i in range(2):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if V[r][c] + A[nr][nc] < V[nr][nc]:
                V[nr][nc] = V[r][c] + A[nr][nc]
                Q.append((nr, nc))

T = int(input())
for tc in range(T):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    V = [[float('inf')] * N for _ in range(N)]
    V[0][0] = A[0][0]
    bfs(0, 0)
    print("#{} {}".format(tc+1, V[N-1][N-1]))