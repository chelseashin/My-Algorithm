# Memoization 풀이

from sys import stdin
input = stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dfs(r, c):
    dp[r][c] = 0
    temp = []
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if not (0 <= nr < N and 0 <= nc < N):
            continue
        # 이동할 곳에 대나무가 더 많고 방문하지 않았다면
        if A[r][c] < A[nr][nc]:
            if dp[nr][nc] == -1:
                dfs(nr, nc)
            temp.append(dp[nr][nc])
    if temp:
        dp[r][c] = max(temp) + 1    # 가장 긴 경로 택하고 + 1 한 값 저장
    else:
        dp[r][c] = 1

# main
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if dp[i][j] == -1:
            dfs(i, j)

maxDis = 0
for i in range(N):
    print(dp[i])
    for j in range(N):
        maxDis = max(maxDis, A[i][j])
print(maxDis)