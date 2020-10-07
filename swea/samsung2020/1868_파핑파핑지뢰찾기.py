import sys
sys.stdin = open('1868_input.txt')
from collections import deque

# 8방향
dr = (-1, 1, 0, 0, -1, 1, 1, -1)
dc = (0, 0, -1, 1, -1, -1, 1, 1)

def bfs(sr, sc):
    cnt = 0
    visited = [[0] * 10 for _ in range(N)]
    visited[sr][sc] = 1
    for v in visited:
        print(v)
    Q = deque([(sr, sc)])
    while Q:
        r, c = Q.popleft()
        bomb = 0
        flag = False
        visited[r][c] = 1
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < 10):
                continue
            if raw[nr][nc] == "*":
                bomb += 1
                flag = True
                print((nr, nc))
                continue
            if visited[nr][nc]:
                continue
            if raw[nr][nc].isdigit():
                continue
            visited[nr][nc] = 1
            Q.append((nr, nc))

        if flag:
            raw[r][c] = bomb
            continue
        else:
            raw[r][c] = 0
            for i in range(8):
                nr = r + dr[i]
                nc = c + dc[i]
                if not (0 <= nr < N and 0 <= nc < 10):
                    continue
                if visited[nr][nc]:
                    continue
                if raw[nr][nc].isdigit():
                    continue
                Q.append((nr, nc))
    print('bomb', bomb)
    for v in visited:
        print(v)
    for r in raw:
        print('new', r)
        # break
    return cnt


# def dfs(depth, blanks):
#     global MIN, A
#     if blanks == 0:
#         MIN = min(MIN, depth)
#         return
#     copyA = [x[:] for x in A]
#     for r in range(N):
#         for c in range(N):
#             if A[r][c] == '.':
#                 temp = bfs(r, c)
#                 dfs(depth+1, blanks-temp)
#                 A = [x[:] for x in copyA]
#                 break

T = int(input())
for tc in range(T):
    N = int(input())
    raw = []
    b = 0
    for i in range(N):
        raw.append(list(input()))
        for j in range(N):
            if raw[i][j] == ".":
                b += 1
        # 지뢰 없는 칸 수
    # for r in raw:
    #     print('raw', r)
    MIN = float('inf')
    # dfs(0, b)
    bfs(2, 2)
    print("#{} {}".format(tc+1, N))

    # AA = [['*', '3', '*'], ['.', '.', '*'], ['*', '*', '.']]
    # print(type(0), type(5), AA[0][1].isdigit())

    # 1 1990
    # 2 1574
    # 3 1252
    # 4 1080
    # 5 7645
    # 6 6378
    # 7 5073
    # 8 4093
    # 9 17111
    # 10 14683
    # 11 11693
    # 12 9135
    # 13 30616
    # 14 26184
    # 15 20124
    # 16 15225
    # 17 48378
    # 18 39769
    # 19 31522
    # 20 24196