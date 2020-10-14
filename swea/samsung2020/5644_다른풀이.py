import sys

sys.stdin = open('5644_input.txt')
from collections import deque

# 상 우 하 좌
dr = (0, -1, 0, 1, 0)
dc = (0, 0, 1, 0, -1)


def install(idx, sr, sc, coverage, performance):
    Q = deque([(sr, sc)])
    raw[idx][sr][sc] = performance
    for _ in range(coverage):
        lq = len(Q)
        for __ in range(lq):
            r, c = Q.popleft()
            for dir in range(1, 5):
                nr = r + dr[dir]
                nc = c + dc[dir]
                if not (0 <= nr < 10 and 0 <= nc < 10):
                    continue
                if raw[idx][nr][nc]:
                    continue
                raw[idx][nr][nc] = performance
                Q.append((nr, nc))


def dfs(depth, total):
    global each, A
    if depth == 2:
        # print(selected)
        each = max(total, each)
        return
    # BC 선택
    for i in range(A):
        if selected[i]:
            continue
        r, c = user[depth][0], user[depth][1]
        if not raw[i][r][c]:
            continue
        selected[i] = 1
        dfs(depth+1, total+raw[i][r][c])
        selected[i] = 0
    dfs(depth+1, total)

# main
T = int(input())
for tc in range(T):
    M, A = map(int, input().split())    # 이동정보 수, 설치된 BC 수
    info = [list(map(int, input().split())) + [0] for _ in range(2)]
    raw = [[[0] * 10 for _ in range(10)] for _ in range(A)]

    MAX = 0
    # BC 정보 저장
    for i in range(A):
        x, y, C, P = map(int, input().split())
        install(i, y-1, x-1, C, P)
    # for R in raw:
    #     for r in R:
    #         print(r)
    #     print()
    user = [[0, 0], [9, 9]]
    selected = [0] * A      # BC 갯수
    for i in range(M+1):
        each = 0
        dfs(0, 0)
        MAX += each
        # print(user)
        for j in range(2):
            user[j][0] += dr[info[j][i]]
            user[j][1] += dc[info[j][i]]
        # print(user, each)
    print("#{} {}".format(tc + 1, MAX))