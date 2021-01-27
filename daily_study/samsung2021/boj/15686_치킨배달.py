# from 11:03 to 11:22
# 19m
# 한 번에 통과
# 특별한 알고리즘 X, combination 함수 + abs 함수로 거리의 절댓값 구함
# M개의 남길 치킨집의 경우의 수를 조합 내장함수로 구하고,
# 집마다 가장 가까운 치킨집까지의 거리를 갱신하여 temp에 담는다.
# temp의 최솟값이 최소 거리

import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())
city = []
chicken = []
houses = []
for i in range(N):
    city.append(list(map(int, input().split())))
    for j in range(N):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

MIN = float('inf')
for comb in list(combinations(chicken, M)):
    temp = 0
    for hr, hc in houses:
        min_dis = float('inf')      # 해당 집과 가능한 치킨집들 사이의 최소 거리
        for cr, cc in comb:
            dis = abs(cr-hr) + abs(cc-hc)
            min_dis = min(min_dis, dis)
        temp += min_dis
    MIN = min(MIN, temp)
print(MIN)