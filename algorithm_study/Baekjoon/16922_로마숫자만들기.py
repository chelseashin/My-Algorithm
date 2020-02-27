N = 2
L = [1, 5, 10, 50]
visited = [0] * 1000
# N = int(input())

# 1
# def dfs(depth):
#     global A, visited
#     if depth == N:
#         t = 0
#         for o in order:
#             t += o
#         visited[t] = 1
#         return
#     for i in L:
#         order.append(i)
#         dfs(depth + 1)
#         order.pop()
#
# order = []
# dfs(0)
# print(sum(visited))

# 2
# import itertools
# per = list(itertools.product(L, repeat = N))
# B = []
# cnt = 0
# for p in per:
#     b = 0
#     for q in p:
#         b += q
#     if b not in B:
#         B.append(b)
#         cnt += 1
# print(B)
# print(cnt)

# 3(성공)
def roma(n, rem, res, card):
    if rem == 0:
        if res not in result:
            result.append(res)
        return
    if card == 4:
        return
    else:
        for i in range(rem+1):
            plus = L[card] * i
            roma(n, rem-i, res+ plus, card+1)

result = []
roma(N, N, 0, 0)
print(result)
print(len(result))