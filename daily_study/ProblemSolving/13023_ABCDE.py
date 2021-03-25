# 5%에서 시간초과
# 20%에서 틀림

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000)

def dfs(depth, start):
    global flag
    print(start)
    if depth >= 4:
        print(depth, visited)
        flag = 1
        return
    for next in info[start]:
        if visited[next]:
            continue
        visited[next] = 1
        dfs(depth+1, next)
        visited[next] = 0

# main
N, M = map(int, input().split())
info = {i: [] for i in range(N)}
for _ in range(M):
    a, b = map(int, input().split())
    info[a].append(b)
    info[b].append(a)

visited = [0] * N
flag = 0
for start in range(N):
    visited[start] = 1
    dfs(0, start)
    visited[start] = 0
    if flag:
        break
if flag:
    print(1)
else:
    print(0)