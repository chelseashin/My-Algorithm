import sys
sys.stdin = open('1868_input.txt')
from collections import deque

# 8방향
dr = (-1, 1, 0, 0, -1, 1, 1, -1)
dc = (0, 0, -1, 1, -1, -1, 1, 1)



# main
T = int(input())
for tc in range(T):
    N = int(input())
    raw = []
    b = 0
    for i in range(N):
        raw.append(list(input()))
        for j in range(N):
            if raw[i][j] == ".":
                b += 1

    print("#{} {}".format(tc+1, raw))