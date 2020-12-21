import sys
sys.stdin = open("3190_input.txt")
from collections import deque
input = sys.stdin.readline

# 우하좌상
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

chD = (1, 2, 3, 0)
chL = (3, 0, 1, 2)

N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1
L = int(input())
info = [list(input().split()) for _ in range(L)]

Q = deque([(0, 0)])
time = 0
idx = 0
dir = 0
while True:
    time += 1
    r, c = Q[0]
    nr = r + dr[dir]
    nc = c + dc[dir]
    # 게임 종료 조건
    if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc] == 2:
        print(time)
        break
    # 빈 공간일 때
    if not board[nr][nc]:
        board[nr][nc] = 2
        Q.appendleft((nr, nc))
        tr, tc = Q.pop()
        board[tr][tc] = 0
    # 사과 있을 때
    if board[nr][nc] == 1:
        board[nr][nc] = 2
        Q.appendleft((nr, nc))

    if time == int(info[idx][0]):   # 방향 전환
        if info[idx][1] == "D":
            dir = chD[dir]
        elif info[idx][1] == "L":
            dir = chL[dir]
        idx = (idx + 1) % L