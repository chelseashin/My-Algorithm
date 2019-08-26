import sys
sys.stdin = open("17_input.txt")

def bfs(s, g):
    global arr, visited, V
    Q = [s]
    visited[s] = 1
    while Q:
        a = Q.pop(0)
        if a == g:
            return
        for i in range(1, V+1):
            if arr[a][i] == 1 and visited[i] == 0:
                visited[i] = visited[a] + 1
                Q.append(i)

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    arr = [[0] * (V+1) for _ in range(V+1)]
    visited = [0] * (V+1)
    for e in range(E):
        start, end = map(int, input().split())
        arr[start][end] = 1
        arr[end][start] = 1
    S, G = map(int, input().split())

    bfs(S, G)
    if visited[G] == 0:
        visited[G] = 1

    print("#{} {}".format(tc+1, visited[G]-1))