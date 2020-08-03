# https://chldkato.tistory.com/114
# https://suri78.tistory.com/4
import sys
sys.stdin = open('1520_input.txt')

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dfs(sr, sc):
    global A, V, M, N
    if sr == M-1 and sc == N-1:
        return 1
    if V[sr][sc] != -1:
        return V[sr][sc]
    V[sr][sc] = 0
    for i in range(4):
        nr = sr + dr[i]
        nc = sc + dc[i]
        if not (0 <= nr < M and 0 <= nc < N):
            continue
        if A[nr][nc] < A[sr][sc]:
            V[sr][sc] += dfs(nr, nc)
    return V[sr][sc]

M, N = map(int, input().split())
A = [list(map(int, input().split())) for i in range(M)]
V = [[-1] * N for _ in range(M)]

print(dfs(0, 0))
print(V)

