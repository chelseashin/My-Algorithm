import sys
sys.stdin = open('17135_input.txt')

from itertools import combinations
from collections import deque

# 적 공격 방향 - 좌, 우, 상
dr = (0, 0, -1)
dc = (-1, 1, 0)

# 궁수 자리 만들기
def set_archer(pos):
    t = [0] * M
    for i in pos:
        t[i] = 2
    field.append(t)
    return [[N, p] for p in pos]

# 적 아래로 한칸씩 이동
def enemy_down():
    field.pop(N-1)
    field.insert(0, [0] * M)

def attack(archer_pos):
    global visited_v
    enemy_pos = set()
    for r, c in archer_pos:
        visited_v += 1
        pos = bfs(r, c)
        if pos:
            enemy_pos.add(pos)
            field[r][c] = 0
    print(field)
    print(enemy_pos)
    print(len(enemy_pos))
    return len(enemy_pos)

def bfs(sr, sc):
    Q = deque()
    visited[sr][sc] = visited_v
    Q.append((sr, sc))
    level = 0
    pos = []
    while Q:
        for _ in range(Q):
            r, c = Q.popleft()
            for i in range(3):
                nr = r + dr[i]
                nc = c + dc[i]
                if not (0 <= nr < N and 0 <= nc < M):
                    continue
                if visited[nr][nc] < visited_v:
                    visited[nr][nc] = visited_v
                    Q.append((nr, nc))
                    if field[nr][nc] == 1:
                        pos.append((nr, nc))
        level += 1
        if pos:
            pos.sort(key=lambda x:x[1])
            return pos[0]
        if level == D:
            if not pos:
                return pos
            pos.sort(key=lambda x:x[1])
            return pos[0]


N, M, D = map(int, input().split())
raw_field = [list(map(int, input().split())) for _ in range(N)]
# print(raw_field)
visited = [[-1] * M for _ in range(N)]
visited_v = 0

max_kill = 0
for pos in combinations(range(M), 3):
    field = raw_field
    archer_pos = set_archer(pos)
    print('archer_pos', archer_pos)
    killed_enemy = 0
    for _ in range(N):
        killed_enemy += attack(archer_pos)
        enemy_down()
    if max_kill < killed_enemy:
        max_kill = killed_enemy

print(max_kill)