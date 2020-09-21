import sys
sys.stdin = open('5650_input.txt')

# 상하좌우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 방향 전환
change = [(),
          (1, 3, 0, 2),
          (3, 0, 1, 2),
          (2, 0, 3, 1),
          (1, 2, 3, 0),
          (1, 0, 3, 2)]

# main
T = int(input())
for tc in range(T):
    N = int(input())
    B = [[5] * (N+2)] + [[5] + list(map(int, input().split())) + [5] for _ in range(N)] + [[5] * (N+2)]
    MAX = float('-inf')
    start = []
    wormhole = {}
    worm_stack = [0] * 11
    for i in range(1, N+1):
        for j in range(1, N+1):
            if not B[i][j]:
                start.append((i, j))
            elif 6 <= B[i][j] <= 10:
                worm_start = worm_stack[B[i][j]]
                if not worm_start:
                    worm_stack[B[i][j]] = (i, j)
                else:
                    wormhole[worm_start] = (i, j)
                    wormhole[(i, j)] = worm_start
    # print(worm_stack)
    # print(wormhole)
    # print(start)
    for sr, sc in start:
        for d in range(4):
            score = 0
            r = sr + dr[d]
            c = sc + dc[d]
            while True:
                # 시작점 또는 블랙홀에 도착하면 탈출
                if (r, c) == (sr, sc) or B[r][c] == -1:
                    break
                if 1 <= B[r][c] <= 5:
                    d = change[B[r][c]][d]
                    score += 1
                elif 6 <= B[r][c] <= 10:
                    r, c = wormhole[(r, c)]
                r += dr[d]
                c += dc[d]
            MAX = max(MAX, score)

    print("#{} {}".format(tc+1, MAX))