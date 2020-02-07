import sys
sys.stdin = open("09_input.txt")

T = int(input())
for tc in range(T):
    str1 = str(input())
    str2 = str(input())
    N, M = len(str1), len(str2)
    ans = 0
    for i in range(M-N+1):
        S = ""
        for j in range(N):
            S += str2[i+j]
        if S == str1:
            ans = 1

    print("#{} {}".format(tc+1, ans))