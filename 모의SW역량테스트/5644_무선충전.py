import sys
sys.stdin = open('5644_input.txt')

T = int(input())
for tc in range(T):
    M, A = map(int, input().split())
    user_a = list(map(int, input().split()))
    user_b = list(map(int, input().split()))
    for _ in range(A):
        X, Y, C, P = map(int, input().split())
        # print(X, Y, C, P)
