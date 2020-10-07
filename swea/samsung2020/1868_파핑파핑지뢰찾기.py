import sys
sys.stdin = open('1868_input.txt')
from collections import deque

# 8방향
dr = (-1, 1, 0, 0, -1, 1, 1, -1)
dc = (0, 0, -1, 1, -1, -1, 1, 1)

def bfs(sr, sc):
    cnt = 0
    Q = deque([(sr, sc)])
    while Q:
        r, c = Q.popleft()
        bomb = 0
        flag = 0
        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if A[nr][nc] != '.':
                if A[nr][nc] == "*":
                    bomb += 1
                    flag = 1
                    continue
                else:
                    continue
        if flag:
            A[r][c] = bomb
            cnt += 1
            continue
            # 8방향 모두 지뢰가 없다면
        # else:
        A[r][c] = 0
        cnt += 1
        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            Q.append((nr, nc))
    # for a in A:
    #     print(a)
    # print(cnt)
    return cnt


def dfs(depth, blanks):
    global MIN, A
    if not blanks:
        MIN = min(MIN, depth)
        return
    copyA = [x[:] for x in A]
    for r in range(N):
        for c in range(N):
            if A[r][c] == '.':
                temp = bfs(r, c)
                dfs(depth+1, blanks-temp)
                A = [x[:] for x in copyA]
                break
                # return

T = int(input())
for tc in range(T):
    N = int(input())
    A = []
    b = 0
    for i in range(N):
        A.append(list(input()))
        for j in range(N):
            if A[i][j] == ".":
                b += 1
    MIN = float('inf')
    dfs(0, b)
    # bfs(0, 0)
    print("#{} {}".format(tc+1, MIN))

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