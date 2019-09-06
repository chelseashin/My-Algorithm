import sys
sys.stdin = open('18_input.txt')

import copy

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 값 땡겨오는 방향
# 상 우 하 좌, 하 우 상 좌
jr = [[-1, 0, 1, 0], [1, 0, -1, 0]]
jc = [[0, 1, 0, -1], [0, 1, 0, -1]]

# 공기청정기 - n은 (r, c)
def clean(n):
    global cleaner, R, C
    r, c = cleaner[n]
    dir = 0
    while True:
        nr = r + jr[n][dir]
        nc = c + jc[n][dir]
        if nr == cleaner[n][0] and nc == cleaner[n][1]:
            new[r][c] =0
            break
        # 아래부분
        if n:
        # 벽 만나면
            if not (cleaner[n][0] <= nr < R and 0 <= nc < C):
                dir += 1
                continue
        # 윗부분
        else:
            if not (0 <= nr < cleaner[n][0] + 1 and 0 <= nc < C):
                dir += 1
                continue
        # 벽 만나지 않을 때
        if new[r][c] != -1:
            new[r][c] = new[nr][nc]
        r = nr
        c = nc

def bfs():
    global arr, new, dust, R, C
    while dust:
        r, c = dust.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            if arr[nr][nc] == -1:
                continue
            if arr[r][c] >= 5:
                new[nr][nc] += arr[r][c] // 5
                new[r][c] -= arr[r][c] // 5

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
new = copy.deepcopy(arr)

cleaner = []
for i in range(R):
    for j in range(C):
        if arr[i][j] == -1:
            cleaner.append((i, j))

dust = []
for t in range(T):
    # 미세먼지 확산
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                dust.append((i, j))
                bfs()

    # 공기청정
    for c in range(len(cleaner)):
        clean(c)
    arr = copy.deepcopy(new)

# print(arr)
mise = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] > 0:
            mise += arr[i][j]
print(mise)