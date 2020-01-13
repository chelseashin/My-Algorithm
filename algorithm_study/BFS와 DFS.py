import sys
sys.stdin = open("sample_input.txt")

# Stack
def dfs(s):
    global N, visited, arr
    S = [s]
    while S:
        start = S.pop()
        if visited[start] == 1:
            continue
        visited[start] = 1
        print(start, end=" ")
        for i in range(N, 0, -1):
            if arr[start][i] == 1 and visited[i] == 0:
                S.append(i)

# 재귀
# def dfs(s):
#     global N, visited, arr
#     visited[s] = 1
#     print(s, end=" ")
#     for i in range(1, N+1):
#         if arr[s][i] == 1 and visited[i] == 0:
#             dfs(i)
# Queue
def bfs(s):
    global N, visited, arr
    visited = [0] * (N + 1)
    Q = [s]
    visited[s] = 1
    while Q:
        start = Q.pop(0)
        print(start, end=" ")
        for i in range(1, N+1):
            if arr[start][i] == 1 and visited[i] == 0:
                visited[i] = 1
                Q.append(i)

N, M, V = map(int, input().split())
arr = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    S, G = map(int, input().split())
    arr[S][G], arr[G][S] = 1, 1
visited = [0] * (N+1)
dfs(V)
print()
bfs(V)