import sys
sys.stdin = open("20056_input.txt")
from collections import deque

# 8방향(0 ~ 7)
dr = (-1, -1, 0, 1, 1, 1, 0, -1)
dc = (0, 1, 1, 1, 0, -1, -1, -1)

def check(L):
    temp = 0
    for t in L:
        temp += t % 2
    if temp == 0 or temp == len(L):
        return True
    return False

# main
N, M, K = map(int, input().split())
Q = deque()
for _ in range(M):
    # 파이어볼의 위치 (r, c), 질량 m, 속력 s, 방향 d
    r, c, m, s, d = map(int, input().split())

    Q.append((r-1, c-1, m, s % N, d))

for k in range(K):
    A = [[[] for _ in range(N)] for _ in range(N)]
    qlen = len(Q)
    print(qlen, Q)
    D = {}
    for _ in range(qlen):
        r, c, m, s, d = Q.popleft()
        # print(r, c, m, s, d)
        nr = (r + dr[d] * s) % N
        nc = (c + dc[d] * s) % N
        if (nr, nc) not in D.keys():
            D[(nr, nc)] = [[m, s % N, d]]
        else:
            D[(nr, nc)] += [[m, s % N, d]]

        # print(r, c, m, "=>", nr, nc, m, s % N, d)
        #
    print(D)
    for key, value in D.items():
        if len(value) > 1:
            tr, tc = key
            vlen = len(value)
            tm, ts = 0, 0
            td = []
            for n in range(vlen):
                tm += value[n][0]
                ts += value[n][1]
                td.append(value[n][2])
            tm //= 5
            ts //= vlen
            if check(td):
                dir = [0, 2, 4, 6]
            else:
                dir = [1, 3, 5, 7]
            print(tm, ts, dir)
            if tm > 0:   # 질량이 0보다 크면
                for dd in dir:
                    Q.append((tr, tc, ))
        # Q.append((nr, nc, m, s % N, d))
        
    print(Q)