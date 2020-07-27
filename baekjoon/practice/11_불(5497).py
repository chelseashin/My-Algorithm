import sys
sys.stdin = open('11_input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def fire(sr, sc):
    global arr, w, h
    Q = [(sr, sc)]
    visited[sr][sc] = 1
    while Q:
        r, c = Q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < h and 0 <= nc < w):
                continue
            if arr[nr][nc] == '#':
                continue
            if arr[nr][nc] == '.' or arr[nr][nc] == '@':
                arr[nr][nc] = '*'
                Q.append((nr, nc))

def move(sr, sc):
    global visited, arr, second, w, h
    Q = [(sr, sc)]
    visited[sr][sc] = 1
    while Q:
        r, c = Q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr == 0 or nr == h-1 or nc == 0 or nc == w-1:
                second += 1
                return
            if not (0 <= nr < h and 0 <= nc < w):
                continue
            if arr[nr][nc] == '*':
                continue
            if arr[nr][nc] == '.':
                visited[nr][nc] = 1
                Q.append((nr, nc))
                second += 1

T = int(input())
for tc in range(T):
    w, h = map(int, input().split())
    arr = [list(input()) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    second = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '*':
                fire(i, j)
            if arr[i][j] == '@':
                move(i, j)


    # if second: ans = second
    # else: ans = "IMPOSSIBLE"

    print("#{} {}".format(tc+1, second))