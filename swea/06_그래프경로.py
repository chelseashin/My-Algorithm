import sys
sys.stdin = open("06_input.txt")


def dfs(x):
    global visited
    if visited[G] == 1:
        return
    for i in range(1, V+1):
        if arr[x][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)


T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    arr = [[0] * (V+1) for _ in range(V+1)]
    for e in range(E):
        start, end = map(int, input().split())
        arr[start][end] = 1
    S, G = map(int, input().split())
    visited = [0] * (V+1)
    dfs(S)

    print("#{} {}".format(tc+1, visited[G]))
