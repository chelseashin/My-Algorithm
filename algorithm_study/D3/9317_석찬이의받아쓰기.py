import sys
sys.stdin = open("9317_input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    S = input()
    R = input()
    cnt = 0
    for i in range(N):
        if S[i] == R[i]:
            cnt += 1
    print("#{} {}".format(tc+1, cnt))