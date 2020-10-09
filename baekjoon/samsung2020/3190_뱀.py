import sys
sys.stdin = open('3190_input.txt')
from collections import deque

# 상하좌우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

chD = (3, 2, 0, 1)
chL = (2, 3, 1, 0)

def move(sr, sc):
    snake = deque([(sr, sc)])
    B[sr][sc] = 2   # 2 : 뱀 표시
    dir = 3     # 오른쪽 방향으로 시작
    idx = 0
    time = 0
    while True:
        r, c = snake[0]
        nr = r + dr[dir]
        nc = c + dc[dir]
        # 벽 만나거나 자기 자신 만나면
        if not (0 <= nr < N and 0 <= nc < N) or (nr, nc) in snake:
            print(time+1)
            return
        if B[nr][nc] == 1:
            B[nr][nc] = 2
            snake.appendleft((nr, nc))

        if B[nr][nc] == 0:
            B[nr][nc] = 2
            snake.appendleft((nr, nc))
            tr, tc = snake.pop()
            B[tr][tc] = 0           # 꼬리 자르기

        time += 1
        t, d = info[idx]
        if time == int(t):      # 방향 바뀔 타이밍이면
            if d == "D":
                dir = chD[dir]
            elif d == "L":
                dir = chL[dir]
            idx = (idx+1) % L

N = int(input())
K = int(input())    # 사과의 갯수
B = [[0] * N for _ in range(N)]
for _ in range(K):
    ar, ac = map(int, input().split())
    B[ar-1][ac-1] = 1
L = int(input())
info = [list(input().split()) for _ in range(L)]    # 뱀의 이동 정보
move(0, 0)