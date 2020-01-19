import sys
sys.stdin = open("11724_input.txt")

# 런타임 에러
def dfs(s):
    global visited, G, N
    for i in range(1, N+1):
        if G[s][i]:
            if visited[i] == 0:
                visited[i] = 1
                dfs(i)
    return

N, M = map(int, input().split())
G = [[0] * (N+1) for _ in range(N+1)]

cnt = 0
for _ in range(M):
    u, v = map(int, input().split())
    G[u][v] = 1
    G[v][u] = 1

visited = [0] * (N + 1)
for i in range(1, N+1):
    if not visited[i]:
        visited[i] = 1
        cnt += 1
        dfs(i)

print(cnt)