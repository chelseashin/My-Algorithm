import sys
sys.stdin = open("3282_input.txt")

# 순열
def comb(depth, k, I):
    global N, M, L, K, MAX
    if depth == I:
        volume = 0
        temp = 0
        # print(order)
        for i in order:
            volume += L[i][0]
            temp += L[i][1]
        if volume > K:
            return
        if temp > MAX:
            MAX = temp
        return
    for i in range(k, N):
        order.append(i)
        comb(depth+1, i+1, I)
        order.pop()

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    L = []
    for _ in range(N):
        V, C = map(int, input().split())
        L.append([V, C])

    MAX = 0
    order = []
    for i in range(1, N+1):
        comb(0, 0, i)

    print("#{} {}".format(tc+1, MAX))