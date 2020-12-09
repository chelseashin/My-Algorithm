import sys
sys.stdin = open('1389_input.txt')

from collections import deque

def bfs(x):
    Q = deque()
    Q.append(x)
    visited = [-1] * N
    visited[x] = 0
    total = 0
    while Q:
        s = Q.popleft()
        for i in G[s]:
            if visited[i] == -1:
                visited[i] = visited[s] + 1
                total += visited[i]
                Q.append(i)
    return total

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

temp = []
for i in range(N):
    temp.append(bfs(i))
print(temp.index(min(temp)) + 1)