import sys
sys.stdin = open('5427_input.txt')

# 성공!
# TC 말고도 반례 생각하면서 문제 풀기

from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 불에 대한 bfs
def Fbfs():
    while FQ:
        r, c = FQ.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < h and 0 <= nc < w):
                continue
            if B[nr][nc] == '#':
                continue
            if fire[nr][nc] >= 0:
                continue
            if B[nr][nc] == '@' or B[nr][nc] == '.' and fire[nr][nc] == -1:
                fire[nr][nc] = fire[r][c] + 1
                FQ.append((nr, nc))
# 사람에 대한 bfs
def Hbfs():
    global dist
    while HQ:
        r, c = HQ.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < h and 0 <= nc < w):
                dist = human[r][c] + 1
                return
            if human[nr][nc] >= 0:
                continue
            if B[nr][nc] == "#":
                continue
            if fire[nr][nc] != -1 and human[r][c] + 1 >= fire[nr][nc]:
                continue
            human[nr][nc] = human[r][c] + 1
            HQ.append((nr, nc))
    dist = "IMPOSSIBLE"
    return

T = int(input())
for tc in range(T):
    w, h = map(int, input().split())
    B = [list(input()) for _ in range(h)]
    fire = [[-1] * w for _ in range(h)]
    human = [[-1] * w for _ in range(h)]
    FQ = deque()
    HQ = deque()
    for i in range(h):
        for j in range(w):
            if B[i][j] == '*':
                FQ.append((i, j))
                fire[i][j] = 0
            if B[i][j] == '@':
                HQ.append((i, j))
                human[i][j] = 0
    Fbfs()
    Hbfs()
    # print('F', fire)
    # print('H', human)
    print(dist)