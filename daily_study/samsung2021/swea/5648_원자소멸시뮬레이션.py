# from 14:15 to 15:10
# 55m
# 메모리, 시간 효율 매우 떨어짐.
# 더 수학적으로 풀 필요 있음..

import sys
sys.stdin = open("5648_input.txt")
from collections import deque

# 상하좌우
dr = (0.5, -0.5, 0, 0)
dc = (0, 0, -0.5, 0.5)

T = int(input())
for tc in range(T):
    N = int(input())
    Q = deque()
    for i in range(N):
        c, r, d, k = map(int, input().split())
        Q.append((r, c, d, k))

    result = 0
    for i in range(4002):
        D = dict()
        qlen = len(Q)
        for _ in range(qlen):
            r, c, d, k = Q.popleft()
            nr = r + dr[d]
            nc = c + dc[d]
            if (nr, nc) not in D:
                D[nr, nc] = [d, k]
            else:
                D[nr, nc][0] = -1       # 충돌한 원자 -1로 표시
                D[nr, nc][1] += k       # 방출한 에너지 더해주기
        for (r, c), (d, k) in D.items():
            if d == -1:
                result += k
            else:
                Q.append((r, c, d, k))
        if not Q:
            break
    print("#{} {}".format(tc+1, result))