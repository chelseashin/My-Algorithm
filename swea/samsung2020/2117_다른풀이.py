import sys
sys.stdin = open('2117_input.txt')

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

KLst = [K * K + (K-1) * (K-1) for K in range(25)]

# main
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    home = []
    for i in range(N):
        for j in range(N):
            if A[i][j]:
                home.append((i, j))
    # print(home)
    MAX = 1
    for size in range(2, N+2):
        for r in range(N):
            for c in range(N):
                cnt = 0
                for i, j in home:
                    if abs(r-i) + abs(c-j) < size:
                        cnt += 1
                if cnt * M >= KLst[size]:
                    MAX = max(cnt, MAX)
    print("#{} {}".format(tc+1, MAX))