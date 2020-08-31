import sys
sys.stdin = open('15686_input.txt')

# Module 사용해서 단순 3중 for문으로 풀기

from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
MIN = float('inf')

chicken = []
house = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))
        if city[i][j] == 2:
            chicken.append((i, j))

for comb in list(combinations(chicken, M)):
    temp = 0
    for r, c in house:
        distance = float('inf')
        for i in range(M):
            distance = min(abs(r-comb[i][0]) + abs(c-comb[i][1]), distance)
        temp += distance
    MIN = min(temp, MIN)

print(MIN)