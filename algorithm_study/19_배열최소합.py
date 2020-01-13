import sys
sys.stdin = open("19_input.txt")

def dfs(depth, temp):
    global N, A, visited, MIN
    # 재귀 시작하자마자 가지치기
    if temp >= MIN:
        return
    if depth == N:
        if temp < MIN:
            MIN = temp
            return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(depth + 1, temp + A[depth][i])
            visited[i] = 0

T = int(input())
for tc in range(T):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N)
    MIN = float('inf')
    dfs(0, 0)    # depth와 temp 모두 0에서 시작
    print("#{} {}".format(tc+1, MIN))