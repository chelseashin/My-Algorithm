import sys
sys.stdin = open("10_input.txt")

def bfs(v):
    global N, A, visited
    visited[v] = 1
    Q = [v]
    while Q:
        start = Q.pop(0)
        print(start, end=' ')
        for i in range(1, N+1):
            if A[start][i] == 1 and visited[i] == 0:
                visited[i] = 1
                Q.append(i)

N, M, V = map(int, input().split())
A = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)

for m in range(M):
    start, end = map(int, input().split())
    A[start][end] = 1
    A[end][start] = 1
bfs(V)

