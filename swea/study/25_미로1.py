import sys
sys.stdin = open("25_input.txt")

# dfs - stack으로 풀기

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(sr, sc):
    global flag, arr
    S = [(sr, sc)]
    while S:
        r, c = S.pop()
        if arr[r][c] == 3:
            flag = 1
            return
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < 16 and 0 <= nc < 16):
                continue
            if arr[nr][nc] == 1:
                continue
            if visited[nr][nc] == 1:
                continue

            S.append((nr, nc))
            visited[nr][nc] = 1

for tc in range(10):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    flag = 0
    dfs(1, 1)

    print("#{} {}".format(N, flag))