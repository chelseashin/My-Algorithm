import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if i % 2 == 1:
            ans += i
        else:
            ans -= i
    print("#{} {}".format(tc+1, ans))