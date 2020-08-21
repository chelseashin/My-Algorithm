import sys
sys.stdin = open('14499_input.txt')

# 1. 리스트 command에는 굴릴 방향을 순서대로 입력하고 리스트 dice는 0으로 초기화한다.
# 2. 명령을 하나씩 불러와서 주사위를 굴린다
#    범위를 벗어나면 continue해서 아무 행동도 하지 않는다
# 3. dice의 인덱스와 방향을 잘 고려해서 굴린 방향에 맞춰 dice를 갱신한다
# 4. 현재 칸이 0이면 주사위 아랫면의 숫자로 바꿔준다
#    0이 아니면 칸의 숫자를 주사위 아랫면으로 옮겨오고 칸의 숫자를 0으로 바꿔준다
# 5. 주사위 윗칸의 숫자를 출력한다

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
    # 주사위 방향에 따라
    if dir == 0:    # 동
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif dir == 1:  # 서
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif dir == 2:  # 북
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    else:           # 남
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

    if not A[nr][nc]:   # 바닥에 값이 없을 때
        A[nr][nc] = dice[5]
    else:               # 값이 있다면
        dice[5] = A[nr][nc]
        A[nr][nc] = 0

    r, c = nr, nc
    print(dice[0])  # 주사위 윗부분의 숫자 출력