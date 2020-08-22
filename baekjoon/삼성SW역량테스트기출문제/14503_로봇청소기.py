import sys
sys.stdin = open('14503_input.txt')

# 시뮬레이션 문제
# 바뀌는 방향에 유의!
# 벽인지 빈공간인지 구별, 이미 청소한 곳이라도 갈 수는 있음
# 후진할 방향 및 종료조건 잘 주기
# 조건 잘 읽고 차근차근 코드로 옮기기

# 북 동 남 서
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

def robot(r, c, d):
    cnt = 1
    while True:
        dir = d
        for i in range(4):    # 순서대로 4방향 탐색
            clean = 0
            dir = (dir-1) % 4
            nr = r + dr[dir]
            nc = c + dc[dir]
            if not (1 <= nr < N-1 and 1 <= nc < M-1):
                continue
            if space[nr][nc]:
                continue
            space[nr][nc] = 2
            cnt += 1
            r, c = nr, nc
            d = dir
            clean = 1
            break
        # 4방향 모두 탐색했을 때 모든 칸이 청소 되어있다면 후진
        if not clean:
            if d == 0:
                r += 1
            elif d == 1:
                c -= 1
            elif d == 2:
                r -= 1
            else:
                c += 1
            # 종료조건 - 후진할 곳이 벽이면 작동 멈춤
            if space[r][c] == 1:
                break
    return cnt

N, M = map(int, input().split())
r, c, d = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]
space[r][c] = 2

print(robot(r, c, d))