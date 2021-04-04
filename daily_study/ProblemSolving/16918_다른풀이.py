from sys import stdin
input = stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def locBombs():
    Q = deque()
    for r in range(R):
        for c in range(C):
            if board[r][c] == "O":
                Q.append((r, c))
    return Q                

def makeBombs():
    for r in range(R):
        for c in range(C):
            if board[r][c] == ".":
                board[r][c] = "O"

def explode():
    global bombs
    while bombs:
        r, c = bombs.popleft()
        board[r][c] = "."
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            board[nr][nc] = "."

# main
R, C, N = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]

N -= 1  # 1초동안 아무것도 하지 않는다.
while N:
    bombs = locBombs()  # 원래 폭탄이 있던 자리
    makeBombs()         # 모든 자리에 폭탄 설치
    N -= 1
    if N == 0:
        break
    explode()           # 폭탄 터짐
    N -= 1

for i in range(R):
    for j in range(C):
        print(board[i][j], end="")
    print()
    