import sys
sys.stdin = open("11724_input.txt")

# 드디어 성공
def dfs(s):
    global visited, G, N
    visited[s] = 1
    for i in G[s]:
        if visited[i] == 0:
            dfs(i)
    return

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
cnt = 0

for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
# print(G)

visited = [0] * (N + 1)
for i in range(1, N+1):
    if visited[i] == 0:
        cnt += 1
        dfs(i)

print(cnt)