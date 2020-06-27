import sys
sys.stdin = open("10_input.txt")

def dfs(s):
    global N, arr, visited
    visited[s] = 1
    for n in range(1, N+1):
        if arr[s][n] == 1 and visited[n] == 0:
            visited[n] = 1
            dfs(n)

N, M = map(int, input().split())
arr = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    u, v = map(int, input().split())
    arr[u][v] = 1
    arr[v][u] = 1

count = 0
for i in range(1, N+1):
    if visited[i] == 0:
        dfs(i)
        count += 1

print(count)