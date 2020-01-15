import sys
sys.stdin = open("2814_input.txt")

# 재귀로 풀기
def dfs(s, temp):
    global A, MAX, visited
    if temp > MAX:
        MAX = temp
    for i in A[s]:
        if not visited[i]:
            visited[i] = 1
            dfs(i, temp+1)
            visited[i] = 0
    return

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    A = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        A[x].append(y)
        A[y].append(x)

    visited = [0] * (N+1)
    MAX = 0
    for i in range(1, N+1):
        visited[i] = 1
        dfs(i, 1)
        visited[i] = 0

    print("#{} {}".format(tc+1, MAX))