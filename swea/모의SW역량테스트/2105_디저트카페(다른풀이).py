import sys
sys.stdin = open('2105_input.txt')

# 우하, 좌하, 좌상, 우상
dr = (1, 1, -1, -1)
dc = (1, -1, -1, 1)

# 시작 좌표, 방향, 들린 카페 리스트, 우하향, 좌하향
def dfs(row, col, dir, cafe, dis1, dis2):
    global MAX, N
    if dir == 4:
        MAX = max(MAX, len(cafe))
        return
    if dir < 2:
        while True:
            if dir == 0:
                dis1 += 1
            if dir == 1:
                dis2 += 1
            row += dr[dir]
            col += dc[dir]
            if (0 <= row < N and 0 <= col < N):
                if raw[row][col] in cafe:
                    return
                cafe += (raw[row][col],)
                dfs(row, col, dir+1, cafe, dis1, dis2)
            else:
                return
    elif dir == 2:
        for i in range(1, dis1+1):
            row += dr[dir]
            col += dc[dir]
            if (0 <= row < N and 0 <= col < N):
                if raw[row][col] in cafe:
                    return
                cafe += (raw[row][col],)
            else:
                return
        dfs(row, col, dir+1, cafe, dis1, dis2)
    elif dir == 3:
        for i in range(1, dis2):
            row += dr[dir]
            col += dc[dir]
            if (0 <= row < N and 0 <= col < N):
                if raw[row][col] in cafe:
                    return
                cafe += (raw[row][col],)
            else:
                return
        dfs(row, col, dir+1, cafe, dis1, dis2)
    return

# main
T = int(input())
for tc in range(T):
    N = int(input())
    raw = [list(map(int, input().split())) for _ in range(N)]
    MAX = -1
    for i in range(N-2):
        for j in range(1, N-1):
            dfs(i, j, 0, (raw[i][j],), 0, 0)

    print("#{} {}".format(tc+1, MAX))

    # 1 6
    # 2 -1
    # 3 4
    # 4 4
    # 5 8
    # 6 6
    # 7 14
    # 8 12
    # 9 18
    # 10 30