import sys
sys.stdin = open("11724_input.txt")

# 시간초과
def dfs(s):
    global visited, G
    S = [s]
    while S:
        now = S.pop()
        for next in G[now]:
            if visited[next]:
                continue
            visited[next] = 1
            S.append(next)
    return

N, M = map(int, input().split())
G = [[] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)
cnt = 0
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
# print(G)

for i in range(1, N+1):
    if visited[i]:
        continue
    visited[i] = 1
    cnt += 1
    dfs(i)

print(cnt)