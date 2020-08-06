import sys
sys.stdin = open('4179_input.txt')

from collections import deque
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 불에 대한 bfs
def Fbfs():
    while Q1:
        r, c = Q1.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            if maze[nr][nc] == "#":
                continue
            if fire[nr][nc] >= 0:
                continue
            if maze[nr][nc] == "J" or maze[nr][nc] == '.':
                fire[nr][nc] = fire[r][c] + 1
                Q1.append((nr, nc))
# 사람에 대한 bfs
def Hbfs():
    global dist
    while Q2:
        r, c = Q2.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < R and 0 <= nc < C):
                dist = human[r][c] + 1
                return
            if maze[nr][nc] == "#":
                continue
            if human[nr][nc] >= 0:
                continue
            if fire[nr][nc] != -1 and human[r][c] + 1 >= fire[nr][nc]:
                continue
            human[nr][nc] = human[r][c] + 1
            Q2.append((nr, nc))
    dist = "IMPOSSIBLE"

R, C = map(int, input().split())
maze = [list(input()) for _ in range(R)]
fire = [[-1] * C for _ in range(R)]
human = [[-1] * C for _ in range(R)]
Q1 = deque()
Q2 = deque()
for i in range(R):
    for j in range(C):
        if maze[i][j] == 'F':
            Q1.append((i, j))
            fire[i][j] = 0
        if maze[i][j] == 'J':
            Q2.append((i, j))
            human[i][j] = 0
print(fire)
Fbfs()
print(human)
Hbfs()
print(dist)