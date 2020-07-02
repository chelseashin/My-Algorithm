import sys
sys.stdin = open("2814_input.txt")

def dfs(s, temp):
    global MAX, N, M, G, visited
    if temp > MAX:
        MAX = temp
    for i in G[s]:
        if visited[i]:
            continue
        visited[i] = 1
        dfs(i, temp + 1)
        visited[i] = 0

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        G[x].append(y)
        G[y].append(x)
    # print(G)

    visited = [0] * (N+1)
    MAX = float('-inf')
    for i in range(1, N+1):
        visited[i] = 1
        dfs(i, 1)
        visited[i] = 0

    print("#{} {}".format(tc+1, MAX))