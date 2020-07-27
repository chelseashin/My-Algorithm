N = 2
# N = int(input())
L = [1, 5, 10, 50]

# 시간초과
# visited = [0] * 1000
# def dfs(depth):
#     if depth == N:
#         S = sum(order)
#         if visited[S] == 0:
#             visited[S] = 1
#         return
#     for i in L:
#         order.append(i)
#         dfs(depth+1)
#         order.pop()
#
# order = []
# dfs(0)
# print(sum(visited))

# 성공
# def roma(n, rem, res, card):
#     if rem == 0:
#         if res not in result:
#             result.append(res)
#         return
#     if card == 4:
#         return
#     else:
#         for i in range(rem+1):
#             plus = L[card] * i
#             roma(n, rem-i, res+ plus, card+1)
#
# # 숫자 조합 리스트(중복 제거)
# result = []
# roma(N, N, 0, 0)
# print(len(result))

# itertools 사용
from itertools import combinations_with_replacement

comb = list(combinations_with_replacement(L, N))
result = set()
for c in comb:
    result.add(sum(c))
print(len(result))