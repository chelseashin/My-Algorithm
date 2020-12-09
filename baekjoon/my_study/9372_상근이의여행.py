import sys
sys.stdin = open('9372_input.txt')
from collections import deque

def bfs(x):
    Q = deque([x])
    visited[x] = 1
    cnt = 0
    while Q:
        x = Q.popleft()
        for nx in G[x]:
            if not visited[nx]:
                visited[nx] = 1
                cnt += 1
                Q.append(nx)
        # print(Q, visited)
    return cnt

# main
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    # print(G)

    visited = [0] * N
    ans = float('inf')
    for i in range(N):
        if not visited[i]:
            ans = min(ans, bfs(i))
    print(ans)