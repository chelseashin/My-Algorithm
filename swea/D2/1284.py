import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    P, Q, R, S, W = map(int, input().split())
    A = P * W
    if W <= R:
        B = Q
    else:
        B = Q + S * (W-R)
    print("#{} {}".format(tc+1, min(A, B)))