import sys
sys.stdin = open("10_input.txt")

def DFS(v):    # v: 시작점

    visit[v] = 1
    print(v, end = ' ')
    for w in G[v]:
        if not visit[w]:
            DFS(w)

V, E, G = map(int, input().split())

G = [[] for _ in range(V+1)]
# print(G)
visit = [0] * (V+1)

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

print(G)
DFS(1)