import sys
sys.stdin = open('08_input.txt')

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(sr, sc):
    global maze, ans
    if ans == 1:
        return
    for i in range(4):
        # if ans == 1:
        #     return
        nr = sr + dr[i]
        nc = sc + dc[i]
        if not (0 <= nr < N and 0 <= nc < N):
            continue
        if maze[nr][nc] == 1:
            continue
        if maze[nr][nc] == 3:
            ans = 1
            return
        maze[nr][nc] = 1
        dfs(nr, nc)

T = int(input())
for tc in range(T):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    ans = 0
    # print(maze)

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                dfs(i, j)

    print("#{} {}".format(tc+1, ans))