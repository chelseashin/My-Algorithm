# Memoization 풀이
# DP 연습 많이 하자..
import sys
input = sys.stdin.readline

direction = [[(0, 1), (1, 1)],
             [(1, 0), (1, 1)],
             [(0, 1), (1, 1), (1, 0)]]

def available(dr, dc):
    if (dr, dc) == (0, 1):      # 가로
        return 0
    elif (dr, dc) == (1, 0):    # 세로
        return 1      
    elif (dr, dc) == (1, 1):    # 대각선
        return 2

# Memoization
def dfs(r, c, d):
    if r == N-1 and c == N-1:
        return 1
    if visited[r][c][d] == -1:
        visited[r][c][d] = 0      # 방문
        for dr, dc in direction[d]:
            nr = r + dr
            nc = c + dc
            nd = available(dr, dc)
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if A[nr][nc]:   # 벽이면
                continue
            if nd == 2 and (A[nr][nc-1] or A[nr-1][nc]):
                continue
            visited[r][c][d] += dfs(nr, nc, nd)
    return visited[r][c][d]

# main
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

visited = [[[-1] * 3 for _ in range(N)] for _ in range(N)]
print(dfs(0, 1, 0))

for v in visited:
    print(v)