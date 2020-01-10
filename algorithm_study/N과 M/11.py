import sys
sys.stdin = open("input2.txt")

def dfs(depth):
    global N, M, A
    if depth == M:
        print(*order)
        return
    for i in range(N):
        order.append(A[i])
        dfs(depth+1)
        order.pop()

N, M = map(int, input().split())
A = sorted(list(set(list(map(int, input().split())))))
N = len(A)
order = []
dfs(0)