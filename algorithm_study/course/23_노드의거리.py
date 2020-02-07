import sys
sys.stdin = open("23_input.txt")

def bfs(s, g):
    global G, visited
    visited[s] = 1
    Q = [s]
    while Q:
        now = Q.pop(0)
        if now == g:
            return
        for i in A[now]:
            if visited[i] == 0:
                visited[i] = visited[now] + 1
                Q.append(i)

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    A = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        A[s].append(e)
        A[e].append(s)
    S, G = map(int, input().split())
    visited = [0] * (V + 1)

    bfs(S, G)
    if not visited[G]:
        visited[G] = 1
    print("#{} {}".format(tc+1, visited[G]-1))