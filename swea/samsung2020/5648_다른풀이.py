import sys
sys.stdin = open('5648_input.txt')

from collections import deque

# 상하좌우
dr = (0.5, -0.5, 0, 0)
dc = (0, 0, -0.5, 0.5)

# main
T = int(input())
for tc in range(T):
    N = int(input())
    Q = deque()
    for i in range(N):
        c, r, d, k = map(int, input().split())
        Q.append((r, c, d, k))
    # print(Q)
    result = 0
    for i in range(4002):
        D = dict()
        while Q:
            r, c, d, k = Q.popleft()
            nr = r + dr[d]
            nc = c + dc[d]
            if (nr, nc) not in D.keys():
                D[(nr, nc)] = [d, k]    # 방향, 크기
            else:
                D[(nr, nc)][0] = -1
                D[(nr, nc)][1] += k
        for (r, c), (d, k) in D.items():
            if d == -1:
                result += k
            else:
                Q.append((r, c, d, k))
        if not Q:
            break

    print("#{} {}".format(tc+1, result))

    # 1 24
    # 2 0
    # 3 8
    # 4 17
    # 5 16
    # 6 10
    # 7 7
    # 8 1111