import sys
sys.stdin = open("11403_input.txt")

def bfs(s):
    global N
    Q = [s]

    while Q:
        tmp = Q.pop(0)
        for t in G[tmp]:
            if visited[t]:
               continue
            visited[t] = 1
            Q.append(t)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
G = [[] for i in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j]:
            G[i].append(j)

for a in range(N):
    visited = [0] * N
    bfs(a)
    print(*visited)