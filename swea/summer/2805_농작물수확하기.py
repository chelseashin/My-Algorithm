import sys
sys.stdin = open("2805_input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    mid = N // 2
    s = mid
    e = mid
    cnt = 0

    for i in range(N):
        if i < mid:
            cnt += sum(farm[i][s:e+1])
            s -= 1
            e += 1
        else:
            cnt += sum(farm[i][s:e+1])
            s += 1
            e -= 1

    print("#{} {}".format(tc+1, cnt))