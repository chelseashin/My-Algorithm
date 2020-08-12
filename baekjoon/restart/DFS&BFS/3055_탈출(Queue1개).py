import sys
sys.stdin = open('3055_input.txt')

# Queue 한 개로 풀기 - 메모리, 시간 조금씩 단축
from collections import deque

# 상하좌우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs():
    while Q:
        r, c, check = Q.popleft()
        # 비버 집에 도착하면 최단거리 리턴
        if raw[r][c] == 'D' and check == 1:
            return visited[r][c]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            if raw[nr][nc] == 'X':
                continue
            if visited[nr][nc] >= 0:
                continue
            # 비버 집 도착했는데 이미 물이 도착했으면
            if raw[nr][nc] == 'D' and check == 0:
                continue
            Q.append((nr, nc, check))
            visited[nr][nc] = visited[r][c] + 1
    return -1

# main
R, C = map(int, input().split())
raw = [list(input()) for _ in range(R)]
Q = deque()
for r in range(R):
    for c in range(C):
        if raw[r][c] == 'S':       # 고슴도치 위치
            sr, sc = r, c
        if raw[r][c] == '*':
            Q.append((r, c, 0))      # 물은 0으로 표시
# 고슴도치는 1로 표시
Q.append((sr, sc, 1))
visited = [[-1] * C for _ in range(R)]
visited[sr][sc] = 0
# print(Q)
# print(visited)
ans = bfs()
# print(visited)
if ans != -1:
    print(ans)
else:
    print('KAKTUS')