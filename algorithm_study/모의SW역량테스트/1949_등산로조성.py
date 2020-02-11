import sys
sys.stdin = open("1949_input.txt")

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dfs(r, c , n):
    global san, N, K

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    san = [list(map(int, input().split())) for tc in range(N)]
    max_dis = float('-inf')
    top = 0
    for i in range(N):
        for j in range(N):
            if san[i][j] > top:
                top = san[i][j]

    for i in range(N):
        for j in range(N):
            if san[i][j] == top:
                visited = [[0] * N for _ in range(N)]
                visited[i][j] = 1
                dfs(i, j, 1)
                visited[i][j] = 0
    print("#{} {}".format(tc+1, max_dis))