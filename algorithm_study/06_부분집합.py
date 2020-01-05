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


# 다른 방법으로 조합 코드 짜보기
def dfs(depth, k):
    global N, K, count
    if depth == N:
        # print(order)
        temp = 0
        for o in order:
            temp += o
        if temp == K:
            count += 1
        return
    for i in range(k, 13):
        order.append(i)
        dfs(depth+1, i+1)
        order.pop()

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    order = []
    count = 0
    dfs(0, 1)
    print("#{} {}".format(tc + 1, count))