# 최소힙 => 파이썬 내장 라이브러리 사용

import sys
input = sys.stdin.readline
import heapq

N = int(input())
hq = []
for _ in range(N):
    num = int(input())
    if num == 0:
        if not hq:
            print(0)
        else:
            print(heapq.heappop(hq))
    else:
        heapq.heappush(hq, num)
