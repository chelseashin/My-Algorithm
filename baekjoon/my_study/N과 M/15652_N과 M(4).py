N, M = 4, 2

# N, M = map(int, input().split())
# 중복조합 구현 기본 코드
def comb(depth, k):
    if depth == M:
        print(*order)
        return
    for i in range(k, N+1):
        order.append(i)
        comb(depth+1, i)
        order.pop()

order = []
comb(0, 1)

# 중복조합 라이브러리로 구현
# from itertools import combinations_with_replacement
# for i in list(combinations_with_replacement(range(1, N+1), M)):
#     print(*i)