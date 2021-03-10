# 21:50 start
# 22:57 finish

import sys
input = sys.stdin.readline

# 상하좌우
direction = ("U", "D", "L", "R")
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
changeDir = ((),
             (3, 2, 1, 0),      # /
             (2, 3, 0, 1))      # \

# 시작 위치, 시작 방향
def signal(sr, sc, sd):
    global max_time, max_dir
    r, c, d = sr, sc, sd
    # print(sr, sc, direction[sd], "방향으로 시작")
    time = 1
    while True:
        r += dr[d]
        c += dc[d]
        if A[r][c] == -1:        # 블랙홀 만났거나 항성계 벗어나면
            if max_time < time:  # 값이 클 때만 갱신
                max_time = time
                max_dir = d

            return
        # 처음 출발한 지점을 동일한 방향으로 접근한 경우
        if (r, c, d) == (sr, sc, sd):
            return
        
        # 방향 전환
        if A[r][c] == 1:
            d = changeDir[1][d]
        elif A[r][c] == 2:
            d = changeDir[2][d]
        time += 1
        # print((r, c), direction[d], time)


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
pr, pc = map(int, input().split())

max_time = float('-inf')
max_dir = -1
for d in range(4):
    signal(pr, pc, d)
    # print("===============", max_time)


if max_time == float('-inf'):
    print("Voyager")
else:
    print(direction[max_dir])
    print(max_time)