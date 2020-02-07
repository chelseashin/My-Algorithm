import sys
sys.stdin = open("14_input.txt")

def dfs(s):
    global arr, V, E
    visited[s] = 1
    print(s, end=" ")
    for i in arr[s]:
        if visited[i] == 0:
            dfs(i)

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V+1)]
    for _ in range(E):
        start, end = map(int, input().split())
        arr[start].append(end)
    S, G = map(int, input().split())
    visited = [0] * (V+1)
    dfs(S)
    print("#{} {}".format(tc+1, visited[G]))