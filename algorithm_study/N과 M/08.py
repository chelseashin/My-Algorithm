import sys
sys.stdin = open("input1.txt")

def dfs(depth, k):
    global N, M, A
    if depth == M:
        print(*order)
        return
    for i in range(k, N):
        order.append(A[i])
        dfs(depth+1, i)
        order.pop()

N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
order = []
dfs(0, 0)