import sys
sys.stdin = open('14499_input.txt')

change=[[3, 1, 0, 5, 4, 2],     #R
        [2, 1, 5, 0, 4, 3],     #L
        [1, 5, 2, 3, 0, 4],     #U
        [4, 0, 2, 3, 5, 1]]     #D

# 동 서 북 남
dr = (0, 0, -1, 1)
dc = (1, -1, 0, 0)

N, M, r, c, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))
dice = [0] * 6

for dir in command:
    dir -= 1
    nr = r + dr[dir]
    nc = c + dc[dir]
    if not (0 <= nr < N and 0 <= nc < M):
        continue
    temp = []
    for i in range(6):
        temp.append(dice[change[dir][i]])
    # print(temp)
    for i in range(6):
        dice[i] = temp[i]

    if A[nr][nc]:
        dice[5] = A[nr][nc]
        A[nr][nc] = 0
    else:
        A[nr][nc] = dice[5]

    r, c = nr, nc
    print(dice[0])