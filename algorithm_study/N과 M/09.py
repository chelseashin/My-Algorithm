import sys
sys.stdin = open("input2.txt")

def dfs(depth):
    global N, M, A
    if depth == M:
        print(*order)
        return

    for i in range(N):
        if visited[i]:
            continue
        if visited[i-1] == 0 and A[i-1] == A[i]:
            continue
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