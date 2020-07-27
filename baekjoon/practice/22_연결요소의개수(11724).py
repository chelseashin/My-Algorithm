import sys

sys.stdin = open('02_input.txt')

def dfs(n):
    global arr, visited
    for i in range(1, N+1):
        if arr[n][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)

N, M = map(int, input().split())
arr = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    u, v = map(int, input().split())
    arr[u][v] = 1
    arr[v][u] = 1

count = 0
for i in range(1, N+1):
    if visited[i] == 1:
        continue
    visited[i] = 1
    dfs(i)
    count += 1

print(count)