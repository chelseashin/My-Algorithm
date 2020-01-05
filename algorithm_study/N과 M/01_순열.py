import sys
sys.stdin = open("input.txt")

# 순열공식

def dfs(depth):
    if depth == M:
        print(*order)
        return
    for i in range(1, N+1):
        if visit[i] == 0:
            visit[i] = 1
            order.append(i)
            dfs(depth+1)
            order.pop()
            visit[i] = 0

N, M = map(int, input().split())
order = []
visit = [0] * (N+1)
dfs(0)