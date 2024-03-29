import sys
input = sys.stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
dirL = (2, 3, 1, 0)
dirR = (3, 2, 0, 1)

T = int(input())
for _ in range(T):
    A = input()
    min_r, min_c, max_r, max_c = 0, 0, 0, 0
    r, c, d = 0, 0, 0
    for cmd in A:
        if cmd == "L":
            d = dirL[d]
            continue
        elif cmd == "R":
            d = dirR[d]
            continue
        elif cmd == "F":
            r += dr[d]
            c += dc[d]
        elif cmd == "B":
            r -= dr[d]
            c -= dc[d]
        min_r = min(min_r, r)
        min_c = min(min_c, c)
        max_r = max(max_r, r)
        max_c = max(max_c, c)

    print(abs(max_r - min_r) * abs(max_c - min_c))