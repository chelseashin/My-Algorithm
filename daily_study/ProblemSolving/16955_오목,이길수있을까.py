# 00:28 start
# 5%에서 틀림.. 내일 보자
# 참고 https://home-body.tistory.com/600

# 왜 틀린지 알겠음.. 이 코드는 더이상 보지 말자.

from sys import stdin
input = stdin.readline

# 8방향
# dr = (0, 1, 1, 1, 0, -1, -1, -1)
# dc = (1, 1, 0, -1, -1, -1, 0, 1)

dr = (-1, 1, 0, 0, -1, 1, -1, 1)
dc = (0, 0, -1, 1, -1, 1, 1, -1)

def check(sr, sc):
    for d in range(8):
        cnt = 1
        r, c = sr, sc
        for _ in range(4):
            r += dr[d]
            c += dc[d]

            if not (0 <= r < 10 and 0 <= c < 10):
                break
            if A[r][c] == "O":
                break
            if A[r][c] == "X":
                cnt += 1
            print((r, c), cnt)
        if cnt >= 4:
            return 1
    return 0

def solve():
    for i in range(10):
        for j in range(10):
            if A[i][j] == "X":
                if check(i, j):
                    return 1
    return 0

A = [list(input().strip()) for _ in range(10)]
print(solve())