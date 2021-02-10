import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    A = [1, 1, 1] + [0] * (N-3)
    for i in range(3, N):
        A[i] = A[i-3] + A[i-2]
    print(A[N-1])