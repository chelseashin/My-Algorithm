import sys
sys.stdin = open("14499_input.txt")
input = sys.stdin.readline

# 동 서 북 남
dr = (0, 0, 0, -1, 1)
dc = (0, 1, -1, 0, 0)

N, M, r, c, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))
dice = [0] * 6
for dir in command:
    nr = r + dr[dir]
    nc = c + dc[dir]
    if not (0 <= nr < N and 0 <= nc < M):
        continue
    if dir == 1:    # 동
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif dir == 2:  # 서
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif dir == 3:  # 북
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    elif dir == 4:  # 남
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

    if A[nr][nc]:
        dice[5] = A[nr][nc]
        A[nr][nc] = 0
    else:
        A[nr][nc] = dice[5]

    r, c = nr, nc
    print(dice[0])