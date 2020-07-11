# 조합(순서 상관 X)
def comb(depth, k):
    if depth == M:
        print(*order)
        return
    for i in range(k, N+1):
        order.append(i)
        comb(depth + 1, i+1)
        order.pop()

N, M = 4, 2
# N, M = map(int, input().split())
order = []
comb(0, 1)

# itertools - 조합 사용
# from itertools import combinations
#
# for i in list(combinations(range(1, N+1), M)):
#     print(*i)