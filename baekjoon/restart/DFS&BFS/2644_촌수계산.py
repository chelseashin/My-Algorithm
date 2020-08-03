import sys
sys.stdin = open('2644_input.txt')

def bfs(start):
    global N, b, M, G
    visited[start] = 1
    Q = [start]
    while Q:
        next = Q.pop(0)
        if next == b:
            return
        for i in G[next]:
            if visited[i]:
                continue
            visited[i] = visited[next] + 1
            Q.append(i)

N = int(input())
a, b = map(int, input().split())
M = int(input())

G = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(M):
    x, y = map(int, input().split())
    G[x].append(y)
    G[y].append(x)
bfs(a)
# print(G)
# print(visited)
print(visited[b]-1)