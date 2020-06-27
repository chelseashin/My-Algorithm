import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    m, d, M, D = map(int, input().split())
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if m == M:
        ans = D-d+1
    else:
        ans = D + (days[m - 1] - d + 1)
        for i in range(m, M-1):
            ans += days[i]
    print("#{} {}".format(tc+1, ans))