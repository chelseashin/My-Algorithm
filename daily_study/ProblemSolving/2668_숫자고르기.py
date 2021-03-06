# 16:20

import sys
input = sys.stdin.readline

# main
n = int(input())
info = {i: int(input())for i in range(1, n+1)}

while True:
    baseSet = set(info.values())
    info = {key: value for key, value in info.items() if key in baseSet}
    # print("딕셔너리 상태", info)
    # print(baseSet, set(info.values()))
    if baseSet == set(info.values()):
        print(len(info))
        for key in info.keys():
            print(key)
        break

# n <= 100이므로 당연히 시간 초과
# from itertools import combinations

# flag = 0
# for i in range(n, 0, -1):
#     for comb in combinations(range(1, n+1), i):
#         temp = set(info[key] for key in comb)
#         if not len(set(comb) - temp):
#             flag = 1
#             print(i)
#             for c in comb:
#                 print(c)
#             break
#     if flag:
#         break