import sys
sys.stdin = open('17837_input.txt')
input = sys.stdin.readline

# 시뮬레이션 문제

# 우, 좌, 상, 하
dr = (0, 0, -1, 1)
dc = (1, -1, 0, 0)

# 방향 전환
rev = (1, 0, 3, 2)

def move(num):
    r, c, d = horse[num]
    nr = r + dr[d]
    nc = c + dc[d]
    # 이동하려는 칸이 맵 벗어나거나 파란색이면
    if not (0 <= nr < N and 0 <= nc < N) or B[nr][nc] == 2:
        d = rev[d]  # 방향 전환
        horse[num][2] = d
        nr = r + dr[d]
        nc = c + dc[d]
        if not (0 <= nr < N and 0 <= nc < N) or B[nr][nc] == 2:
            return 0
    # 이동시키는 말 리스트
    pieces = []
    for i, key in enumerate(board[r][c]):
        if key == num:
            pieces.extend(board[r][c][i:])
            board[r][c] = board[r][c][:i]
            break
    # 이동하려는 칸이 빨간색이면
    if B[nr][nc] == 1:
        pieces.reverse()
    for i in pieces:
        board[nr][nc].append(i)
        horse[i][:2] = [nr, nc]
    if len(board[nr][nc]) >= 4:
        return 1
    return 0

# main
N, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]
board = [[[] for _ in range(N)] for _ in range(N)]
horse = [[] for _ in range(K)]  # 말의 위치

for i in range(K):
    r, c, d = map(int, input().split())
    board[r-1][c-1].append(i)
    horse[i] = [r-1, c-1, d-1]
# print(board)
# print(horse)

turn = 1
flag = 0
while True:
    if turn > 1000:
        print(-1)
        break
    for i in range(K):
        flag = move(i)
        if flag:
            print(turn)
            exit()
    turn += 1