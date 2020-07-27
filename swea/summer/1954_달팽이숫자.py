import sys
sys.stdin = open("1954_input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    r, c = 0, -1
    num = 0
    cnt = N
    arr = [[0] * N for _ in range(N)]

    while num < N * N:
        # 오른쪽 방향
        for i in range(cnt):
            c += 1
            num += 1
            arr[r][c] = num
        cnt -= 1
        # 아래쪽
        for i in range(cnt):
            r += 1
            num += 1
            arr[r][c] = num
        # 왼쪽
        for i in range(cnt):
            c -= 1
            num += 1
            arr[r][c] = num
        cnt -= 1
        # 위쪽
        for i in range(cnt):
            r -= 1
            num += 1
            arr[r][c] = num
    print("#{}".format(tc+1))
    for i in arr:
        print(*i)
    # print(arr)