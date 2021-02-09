# 문제 유형 : 힙, 자료구조, 그리디
# 가장 크기가 작은 숫자 묶음들을 먼저 합쳤을 때 비교 횟수가 가장 적음

import sys
input = sys.stdin.readline
import heapq

N = int(input())
hq = []
for _ in range(N):
    heapq.heappush(hq, int(input()))

result = 0
while len(hq) != 1:
    a = heapq.heappop(hq)
    b = heapq.heappop(hq)
    sum_ab = a + b
    result += sum_ab
    heapq.heappush(hq, sum_ab)
print(result)