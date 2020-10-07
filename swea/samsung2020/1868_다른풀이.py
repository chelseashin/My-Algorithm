import sys
sys.stdin = open('1868_input.txt')
from collections import deque

# 8방향
di = [-1, -1, -1, 0, 1, 1, 1, 0]
dj = [-1, 0, 1, 1, 1, 0, -1, -1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    game = [list(input()) for x in range(N)]
    # '*' : 지뢰 있음 / '.' : 지뢰없음
    # 클릭수 세기
    click = 0
    for i in range(N):
        for j in range(N):
            if game[i][j] == '*':
                for k in range(8):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < N and 0 <= nj < N and game[ni][nj] != "*":
                        if game[ni][nj] == ".":
                            game[ni][nj] = 0
                        game[ni][nj] += 1
            elif game[i][j] == ".":
                game[i][j] = 0
    zero = deque()
    for i in range(N):
        for j in range(N):
            if game[i][j] == 0:
                zero.append([i, j])
                click += 1
                while zero:
                    # print(zero)
                    pick = zero.popleft()
                    x, y = pick
                    game[x][y] = '*'
                    for k in range(8):
                        ni = x + di[k]
                        nj = y + dj[k]
                        if 0 <= ni < N and 0 <= nj < N:
                            if game[ni][nj] != '*':
                                if game[ni][nj] == 0:
                                    zero.append((ni, nj))
                                game[ni][nj] = '*'
    for i in range(N):
        for j in range(N):
            if game[i][j] != '*':
                click += 1
    print('#{} {}'.format(tc, click))

    # 1 1990
    # 2 1574
    # 3 1252
    # 4 1080
    # 5 7645
    # 6 6378
    # 7 5073
    # 8 4093
    # 9 17111
    # 10 14683
    # 11 11693
    # 12 9135
    # 13 30616
    # 14 26184
    # 15 20124
    # 16 15225
    # 17 48378
    # 18 39769
    # 19 31522
    # 20 24196