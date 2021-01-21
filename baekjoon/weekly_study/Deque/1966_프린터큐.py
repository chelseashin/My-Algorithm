import sys
sys.stdin = open('1966_input.txt')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    L = list(map(int, input().split()))
    # print(N, M, L)
    Q = [(i, v) for i, v in enumerate(L)]
    print(Q)
    cnt = 0
    while True:
        if Q[0][1] == max(Q, key=lambda x: x[1])[1]:
            cnt += 1

            if Q[0][0] == M:
                print(cnt)
                break
            else:
                Q.pop(0)
        else:
            Q.append(Q.pop(0))
        # print(Q)