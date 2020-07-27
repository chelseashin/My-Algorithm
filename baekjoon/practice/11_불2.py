import sys
sys.stdin = open('11_input.txt')
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    global result
    while man:
        result += 1
        fire_time = len(fire)
        for i in range(fire_time):
            r, c = fire.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if not (0 <= nr < h and 0 <= nc < w):
                    continue
                if arr[nr][nc] == '.' or arr[nr][nc] == '@':
                    arr[nr][nc] = '*'
                    fire.append((nr, nc))

        man_time = len(man)
        for i in range(man_time):
            r, c = man.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if not (0 <= nr < h and 0 <= nc < w):
                    return
                # if visited[nr][nc]:
                #     continue
                if arr[nr][nc] == '.':
                    arr[nr][nc] = '@'
                    # visited[nr][nc] = visited[r][c] + 1
                    man.append((nr, nc))
    result = 'IMPOSSIBLE'


T = int(input())
for tc in range(T):
    w, h = map(int, input().split())
    arr = [list(input()) for _ in range(h)]
    # visited = [[0] * w for _ in range(h)]
    man = deque()
    fire = deque()
    result = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '@':
                man.append((i, j))
                # visited[i][j] = 1
            elif arr[i][j] == '*':
                fire.append((i, j))
    bfs()
    # if result == 0:
    #     result = 'IMPOSSIBLE'
    print("#{} {}".format(tc+1, result))
