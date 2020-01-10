import sys
sys.stdin = open("input2.txt")

def comb(depth, k):
    global N, M, A, S, visited
    if depth == M:
        print(*order)
        return
    for i in range(k, N):
        if visited[i]:
            continue
        if i > 0 and visited[i-1] == 0 and A[i-1] == A[i]:
            continue
        order.append(A[i])
        visited[i] = 1
        comb(depth+1, i+1)
        order.pop()
        visited[i] = 0

N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
order = []
visited = [0] * (N)
comb(0, 0)