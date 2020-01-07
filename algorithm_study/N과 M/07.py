import sys
sys.stdin = open("input1.txt")

def dfs(depth):
    global N, M, A
    if depth == M:
        print(*order)
        return
    for i in range(N):
        visited[i] = 1
        order.append(A[i])
        dfs(depth+1)
        order.pop()
        visited[i] = 0

N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
order = []
visited = [0] * (N+1)
dfs(0)