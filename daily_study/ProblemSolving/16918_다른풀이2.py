# 성공 풀이

from sys import stdin
input = stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# main
R, C, N = map(int, input().split())
board = [list(input()) for _ in range(R)]

if N % 2 == 0:
    for _ in range(R):
        print('O' * C)
elif N == 1:
    for i in range(R):
        for j in range(C):
            print(board[i][j], end="")
        print()
else:
    bomb = []
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'O':
                bomb.append((i, j))
            else:
                board[i][j] = 'O'

    while bomb:
        r, c = bomb.pop()
        board[r][c] = '.'
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < R and 0 <= nc < C:
                board[nr][nc] = '.'

    if (N - 2) % 4 == 1:
        for i in range(R):
            for j in range(C):
                print(board[i][j], end="")
            print()
    else:
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O':
                    bomb.append((i, j))
                else:
                    board[i][j] = 'O'
                    
        while bomb:
            r, c = bomb.pop()
            board[r][c] = '.'
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < R and 0 <= nc < C:
                    board[nr][nc] = '.'
        for i in range(R):
            for j in range(C):
                print(board[i][j], end="")
            print()