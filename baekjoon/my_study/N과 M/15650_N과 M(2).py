# N, M = map(int, input().split())

# 조합 구현 기본 코드
N, M = 4, 2

def perm(depth, k):
    if depth == M:
        print(*order)
        return
    for i in range(k, N+1):
        order.append(i)
        perm(depth+1, i+1)
        order.pop()

order = []
# perm(0, 1)

# 조합 라이브러리 사용 기본 코드
from itertools import combinations
for x in list(combinations(range(1, N+1), M)):
    print(*x)