import sys
sys.stdin = open('2105_input.txt')

# 디저트카페
# backtracking

dr = (1, 1, -1, -1)
dc = (1, -1, -1, 1)

def check(r, c, num):
    global MAX
    cafe = []
    cnt = 0
    for i in range(4):  # 마름모 각 변의 길이
        for _ in range(num[i]):
            r += dr[i]
            c += dc[i]
            if A[r][c] not in cafe:
                cafe.append(A[r][c])
                cnt += 1
            else:
                return
    MAX = max(MAX, cnt)
    # print(MAX)

def dfs(r, c, dir):
    if dir == 3:
        if num[0] != num[2]:
            return
    if dir == 4:
        if num[0] == num[2] and num[1] == num[3]:
            # print(sr, sc, num)
            check(sr, sc, num)
        return
    # 가능한 모든 변의 길이
    for i in range(N-1, 0, -1):
        nr = r + dr[dir] * i
        nc = c + dc[dir] * i
        if not (0 <= nr < N and 0 <= nc < N):
            continue
        num[dir] = i
        dfs(nr, nc, dir+1)


# main
T = int(input())
for tc in range(T):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    num = [0] * 4
    MAX = -1
    for i in range(N-2):
        for j in range(1, N-1):
            sr, sc = i, j
            dfs(sr, sc, 0)
    print("#{} {}".format(tc + 1, MAX))
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