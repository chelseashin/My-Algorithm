import sys
sys.stdin = open("24_input.txt")

import itertools

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    for i in range(1, N+1):
        sum = 0
        L = list(itertools.combinations(A, i))

        for s in L:
            Sum = 0
            for n in s:
                Sum += n
            if Sum == K:
                count += 1
    print("#{} {}".format(tc+1, count))



# TC는 맞으나 정답 20개 모두 틀림
# def comb(depth, k, p):
#     global N, K, count
#     if depth == p:
#         # print(order)
#         total = 0
#         for o in order:
#             total += A[o]
#         if total == K:
#             count += 1
#         return
#     for i in range(k, N):
#         order.append(i)
#         comb(depth+1, i+1, p)
#         order.pop()
#
# T = int(input())
# for tc in range(T):
#     N, K = map(int, input().split())
#     A = list(map(int, input().split()))
#
# order= []
# count = 0
# for n in range(1, N+1):
#     comb(0, 0, n)
# print("#{} {}".format(tc+1, count))