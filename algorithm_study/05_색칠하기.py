import sys
sys.stdin = open("05_input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]
    for _ in range(N):
        r1, c1, r2, c2, color = list(map(int, input().split()))
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                arr[i][j] += color
    count = 0
    for r in range(10):
        for c in range(10):
            if arr[r][c] == 3:
                count += 1
    print("#{} {}".format(tc+1, count))