import sys
sys.stdin = open("5099_input.txt")

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    P = []
    for i in range(M):
        c = [i+1, C[i]]
        P.append(c)

    Q = P[:N]
    Q1 = P[N:]
    # idx = N
    while Q:
        for i in range(N):
            if Q[i][1] // 2 > 0:
                Q[i][1] = Q[i][1] // 2
            else:
                Q.pop(i)
                try:
                    Q.insert(i, Q1.pop(0))
                except:
                    continue

        if len(Q) < N:
            N = len(Q)


    print("#{} {}".format(tc+1, Q[0][0]))