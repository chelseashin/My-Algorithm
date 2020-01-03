import sys
sys.stdin = open("06_input.txt")

# 조합으로 문제 풀기

# import itertools
# T = int(input())
# for tc in range(T):
#     N, K = map(int, input().split())
#     cnt = 0
#     A = list(range(1, 13))
#     C = list(itertools.combinations(range(1, 13), N))
#
#     for temp in C:
#         SUM = 0
#         for i in temp:
#             SUM += i
#         if SUM == K:
#             cnt += 1
#     print("#{} {}".format(tc+1, cnt))

def dfs(depth, k):
    global N, K
    if depth == N:


    for i in range(k, 12):

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())