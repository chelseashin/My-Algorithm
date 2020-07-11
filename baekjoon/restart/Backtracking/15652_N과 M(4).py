# 중복 조합(순서 상관 X)
def comb(depth, k):
    if depth == M:
        print(*order)
        return
    for i in range(k, N+1):
        order.append(i)
        comb(depth + 1, i)
        order.pop()

N, M = 4, 2
# N, M = map(int, input().split())
order = []
comb(0, 1)

# itertools - 조합 사용(시간, 메모리 단축)
# from itertools import combinations_with_replacement
#
# for i in list(combinations_with_replacement(range(1, N+1), M)):
#     print(*i)