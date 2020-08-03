import sys
sys.stdin = open('7562_input.txt')

from collections import deque

dr = (-2, -1, 1, 2, 2, 1, -1, -2)
dc = (1, 2, 2, 1, -1, -2, -2, -1)

def bfs(sr, sc):
    global N, A, gr, gc
    Q = deque([(sr, sc)])
    A[sr][sc] = 1
    while Q:
        r, c = Q.popleft()
        if r == gr and c == gc:
            return
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if A[nr][nc]:
                continue
            A[nr][nc] = A[r][c] + 1
            Q.append((nr, nc))

T = int(input())
for tc in range(T):
    N = int(input())
    A = [[0] * N for _ in range(N)]
    sr, sc = map(int, input().split())
    gr, gc = map(int, input().split())
    bfs(sr, sc)
    # print(A)
    print(A[gr][gc]-1)
