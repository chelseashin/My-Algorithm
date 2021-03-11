# 21:50 start
# 22:57 finish
# 50%에서 틀림..

import sys
input = sys.stdin.readline

# 상하좌우
direction = ("U", "D", "L", "R")
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
changeDir = ((),
             (3, 2, 1, 0),      # /
             (2, 3, 0, 1))      # \

def signal():
    max_time = 0
    max_dir = 0

    for sd in range(4):
        r, c, d = sr, sc, sd    # 시작 위치, 시작 방향
        time = 1
        # print(sr, sc, direction[sd], "방향으로 시작")
        while True:
        # while A[r+dr[d]][c+dc[d]] != -1:
            if A[r+dr[d]][c+dc[d]] == -1:    # 블랙홀 만났거나 항성계 벗어나면
                break
            r += dr[d]
            c += dc[d]

            # 방향 전환
            if A[r][c] == 1:
                d = changeDir[1][d]
            elif A[r][c] == 2:
                d = changeDir[2][d]
            time += 1

            # 처음 출발한 지점을 동일한 방향으로 접근한 경우 무한 루프
            if (r, c, d) == (sr, sc, sd):
                print(direction[sd])
                print("Voyager")
                return
            # print((r, c), direction[d], time)
        if max_time < time:  # 값이 클 때만 갱신
            max_time = time
            max_dir = sd

    print(direction[max_dir])
    print(max_time)


# main
N, M = map(int, input().split())
A = [[-1] * (M+2) for _ in range(N+2)]
star_system = []
for i in range(N):
    star_system.append(input())
    for j in range(M):
        if star_system[i][j] == ".":    # 빈 공간
            A[i+1][j+1] = 0
        elif star_system[i][j] == "C":  # 블랙홀
            A[i+1][j+1] = -1
        elif star_system[i][j] == "/":  # /
            A[i+1][j+1] = 1
        else:
            A[i+1][j+1] = 2             # \
sr, sc = map(int, input().split())

signal()