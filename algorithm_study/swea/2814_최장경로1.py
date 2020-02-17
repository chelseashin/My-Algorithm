import sys
sys.stdin = open("2814_input.txt")

# 재귀로 풀기
def dfs(s, temp):
    global A, MAX
    visited[s] = 1
    for i in range(1, N):
        if i == s:
            continue
        if visited[i]:
            continue
        if not A[s][i]:
            continue
        dfs(i, temp + 1)
        visited[i] = 0
    if temp > MAX:
        MAX = temp
    return

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    A = [[0] * (N+1) for _ in range(N+1)]
    MAX = float('-inf')
    for _ in range(M):
        x, y = map(int, input().split())
        A[x][y] = 1
        A[y][x] = 1
    for i in range(1, N+1):
        visited = [0] * (N + 1)
        dfs(i, 1)

    print("#{} {}".format(tc+1, MAX))