import sys
sys.stdin = open('02_input.txt')

# DFS
def dfs(v):
    global A, visited
    stack = [v]
    while stack:
        now = stack.pop()
        for next in A[now]:
            if visited[next] == 1:
                continue
            visited[next] = 1
            stack.append(next)
    return

N, M = map(int, input().split())
A = [[] for _ in range(N+1)]
visited = [0] * (N+1)
count = 0
for i in range(M):
    u, v = map(int, input().split())
    A[u].append(v)
    A[v].append(u)
# print(A)

for j in range(1, N+1):
    if visited[j] == 1:
        continue
    visited[j] = 1
    count += 1
    dfs(j)

print(count)