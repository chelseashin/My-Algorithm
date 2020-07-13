import sys
sys.stdin = open('1260_input.txt')

def dfs(s):
    global N, G, visited
    visited[s] = 1
    print(s, end=" ")
    for i in range(1, N+1):
        if G[s][i] == 1 and visited[i] == 0:
            dfs(i)

def bfs(s):
    global N, G, visited
    visited[s] = 1
    Q = [s]
    while Q:
        start = Q.pop(0)
        print(start, end=" ")
        for i in range(1, N+1):
            if visited[i] == 0 and G[start][i] == 1:
                visited[i] = 1
                Q.append(i)

N, M, V = map(int, input().split())
G = [[0] * (N+1) for _ in range((N+1))]
for _ in range(M):
    start, end = map(int, input().split())
    G[start][end] = 1
    G[end][start] = 1
print(G)

visited = [0] * (N+1)
dfs(V)
print()
visited = [0] * (N+1)
bfs(V)