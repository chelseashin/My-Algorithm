import sys
sys.stdin = open("02_input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if i % 2:
            ans += i
        else:
            ans -= i

    print("#{} {}".format(tc+1, ans))