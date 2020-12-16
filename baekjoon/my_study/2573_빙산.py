import sys
sys.stdin = open('2573_input.txt')
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)



# main
N, M = map(int, input().split())
iceburg = [list(map(int, input().split())) for _ in range(N)]
print(iceburg)

time = 0

while True:
    cnt = 0

    for i in range(N):
        for j in range(M):
            if iceburg[i][j]:



    if cnt >= 2:
        print(time)
        break