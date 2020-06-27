import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N > M:
        N, M = M, N
        A, B = B, A
    MAX = float('-inf')
    for i in range(M-N+1):
        temp = 0
        for j in range(N):
            temp += A[j] * B[i+j]
        if temp > MAX:
            MAX = temp
    print("#{} {}".format(tc+1, MAX))