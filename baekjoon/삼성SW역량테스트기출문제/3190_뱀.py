import sys
sys.stdin = open('3190_input.txt')

# 주어진 조건을 그대로 구현하는 시뮬레이션 문제
# 뱀이 사과를 먹으면서 길이를 늘리는 게임을 구현해야 한다.
#
# 뱀의 시작 위치는 (0, 0)이며 시작 방향은 오른쪽이다. 범위 (0, 0) ~ (N-1, M-1) 기준
# 뱀의 이동 좌표를 저장하기 위해 Queue를 사용한다.
# 매초, 뱀이 현재 방향으로 머리를 먼저 한 칸 앞으로 옮긴다. 머리 위치를 큐에 push 한다.
# 이동한 칸에 사과(1)가 있을 경우, 꼬리를 줄이지 않는다.
# 이동한 칸이 빈칸(0)이라면, 꼬리를 한 칸 줄인다. 큐에서 꼬리 칸을 pop 한다.
# 뱀의 좌표는 (2)로 둔다.
# 이동 후에, 방향 전환을 해야 한다면, 주어진 입력에 따라 방향을 바꾼다.
# 이동할 때 벽에 부딪히거나(맵을 벗어난 경우), 뱀 자신(2)에게 부딪히면 종료한다.
# 그렇지 않다면 시간을 1초 증가시키고, 위 과정을 반복한다.

from collections import deque

# 우좌하상
dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)
# 상하좌우 잘 따지기
L = (3, 2, 0, 1)
D = (2, 3, 1, 0)

def solve():
    global seconds
    sr, sc = 0, 0
    dir, d = 0, 0
    board[sr][sc] = 2
    Q = deque([(sr, sc)])
    while True:
        sr = sr + dr[dir]
        sc = sc + dc[dir]
        seconds += 1
        # 종료조건 : 벽 만나거나 자기 자신을 만나면 리턴
        if not (0 <= sr < N and 0 <= sc < N):
            return
        if board[sr][sc] == 2:
            return
        if not board[sr][sc]:
            nr, nc = Q.popleft()
            board[nr][nc] = 0
        board[sr][sc] = 2
        Q.append((sr, sc))

        t, c = dir_info[d]
        # 방향 바뀔 타이밍이면
        if seconds == int(t):
            if c == 'L':    # 왼쪽일 때
                dir = L[dir]
            else:           # 오른쪽일 때
                dir = D[dir]
            d = (d+1) % M

# main
N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1
# print(board)

M = int(input())
dir_info = [list(input().split()) for _ in range(M)]
# print(dir_info)

# 경기 끝날 때까지 뱀 움직이기
seconds = 0
solve()
# print(board)
print(seconds)