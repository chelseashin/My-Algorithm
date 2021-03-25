# Memoization 풀이
# https://hjp845.tistory.com/178

from sys import stdin
input = stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dfs(r, c):
    if dp[r][c] > -1:
        print((r, c))
        for dd in dp:
            print(dd)
        print()
        return dp[r][c]
    dp[r][c] = 0
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if not (0 <= nr < N and 0 <= nc < N):
            continue
        # 이동할 곳에 대나무가 더 많다면
        if A[r][c] < A[nr][nc]:
            dp[r][c] = max(dp[r][c], dfs(nr, nc))
    dp[r][c] += 1
    return dp[r][c]

# main
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1] * N for _ in range(N)]
maxDis = 0
for i in range(N):
    for j in range(N):
        maxDis = max(maxDis, dfs(i, j))
print(maxDis)