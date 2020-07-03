import sys
sys.stdin = open('4881_input.txt')

def dfs(depth, temp):
    global N, A, visited, MIN
    if temp >= MIN:
        return
    if depth == N:
        if temp < MIN:
            MIN = temp
            return
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = 1
        dfs(depth+1, temp + A[depth][i])
        visited[i] = 0

T = int(input())
for tc in range(T):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    MIN = float('inf')
    dfs(0, 0)
    print("#{} {}".format(tc+1, MIN))