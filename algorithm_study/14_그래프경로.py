import sys
sys.stdin = open("14_input.txt")

def dfs(s):
    global visited
    visited[s] = 1
    for i in range(1, V+1):
        if arr[s][i] and visited[i] == 0:
            dfs(i)

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    arr = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        start, end = map(int, input().split())
        arr[start][end] = 1
    S, G = map(int, input().split())
    visited = [0] * (V+1)
    dfs(S)

    print("#{} {}".format(tc+1, visited[G]))