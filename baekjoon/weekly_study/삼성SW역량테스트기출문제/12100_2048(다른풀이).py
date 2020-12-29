import sys
sys.stdin = open("12100_input.txt")
input = sys.stdin.readline
from collections import deque

# 시작 좌표, 합치는 방향
def merge(r, c, dr, dc):
    global MAX
    while Q:
        x = Q.popleft()
        if not board[r][c]:     # 빈 칸이면
            board[r][c] = x     # 그대로 놓기
            MAX = max(MAX, x)
        elif board[r][c] == x:  # 같은 값이면
            board[r][c] *= 2    # 이전에 놓은 블록의 값에 2배
            MAX = max(MAX, board[r][c])
            r += dr             # 다음 블록을 놓을 위치
            c += dc
        else:                   # 다른 값이면
            r += dr
            c += dc
            board[r][c] = x     # 한칸 뒤에 놓기
            MAX = max(MAX, x)

# 상하좌우로 판 움직이기
def move(dir):
    if dir == 0:    # 상
        for j in range(N):
            for i in range(N):
                if board[i][j]:
                    Q.append(board[i][j])
                    board[i][j] = 0     # Q에 넣은 블록은 0으로 바꿔주기
            merge(0, j, 1, 0)       # 시작 좌표, 합치는 방향(아래)

    elif dir == 1:      # 하
        for j in range(N):
            for i in range(N-1, -1, -1):
                if board[i][j]:
                    Q.append(board[i][j])
                    board[i][j] = 0
            merge(N-1, j, -1, 0)

    elif dir == 2:      # 좌
        for i in range(N):
            for j in range(N-1, -1, -1):
                if board[i][j]:
                    Q.append(board[i][j])
                    board[i][j] = 0
            merge(i, N-1, 0, -1)

    elif dir == 3:      # 우
        for i in range(N):
            for j in range(N):
                if board[i][j]:
                    Q.append(board[i][j])
                    board[i][j] = 0
            merge(i, 0, 0, 1)

def dfs(depth):
    global MAX, board
    if depth == 5:
        return
    B = [x[:] for x in board]
    for d in range(4):
        move(d)
        dfs(depth + 1)
        board = [x[:] for x in B]

# main
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
MAX = 0
Q = deque()
dfs(0)
print(MAX)
