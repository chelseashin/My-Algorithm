import sys
sys.stdin = open("2814_input.txt")

# 재귀로 풀기
def dfs(a, b):
    global A, MAX, temp, visited

    visited[a] = 1
    for n in range(1, N+1):
        if A[b][n] and visited[n] == 0:
            # visited[n] = 1
            temp += 1
            dfs(n, b)

    if temp > MAX:
        MAX = temp
    return


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    A = [[0] * (N+1) for _ in range(N+1)]
    S = set()
    for _ in range(M):
        x, y = map(int, input().split())
        S.add(x)
        S.add(y)
        A[x][y] = 1
        A[y][x] = 1
    print(S)
    MAX = float('-inf')
    for i in range(1, N+1):
        for j in range(1, N+1):

            if A[i][j]:
                temp = 1
                visited = [0] * (N+1)
                dfs(i, j)

    print("#{} {}".format(tc+1, MAX))