# 1h 40m
import sys
sys.stdin = open("14503_input.txt")
input = sys.stdin.readline

# 북 동 남 서
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)
chd = (3, 0, 1, 2)

# main
N, M = map(int, input().split())
r, c, d = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
A[r][c] = 2
cnt = 1
while True:
    for i in range(4):
        d = chd[d]
        nr = r + dr[d]
        nc = c + dc[d]
        if A[nr][nc]:
            continue
        if not A[nr][nc]:
            cnt += 1
            A[nr][nc] = 2   # 청소공간 표시
            r, c = nr, nc   # 이동
            break
    else:                   # 위 for 문에서 아무것도 걸리지 않으면 후진 실행
        nr = r - dr[d]
        nc = c - dc[d]
        if A[nr][nc] == 2:
            r, c = nr, nc
            continue
        elif A[nr][nc] == 1:    # 뒤쪽 방향 벽이면 후진 X
            print(cnt)
            break