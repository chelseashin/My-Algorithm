import sys
sys.stdin = open("7465_input.txt")

def dfs(v):
    global G, visited
    visited[v] = 1
    for i in G[v]:
        if visited[i]:
            continue
        visited[i] = 1
        dfs(i)

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    for _ in range(M):
        s, e = map(int, input().split())
        G[s].append(e)
        G[e].append(s)
    # print(G)
    count = 0
    for i in range(1, N+1):
        if visited[i]:
            continue
        count += 1
        dfs(i)

    print("#{} {}".format(tc+1, count))