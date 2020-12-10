N, M = 3, 3

# N, M = map(int, input().split())
# 중복순열 구현 기본 코드
def perm(depth):
    if depth == M:
        print(*order)
        return
    for i in range(1, N+1):
        order.append(i)
        perm(depth+1)
        order.pop()

order = []
# perm(0)

# 중복순열 라이브러리 사용 기본 코드
from itertools import product
for i in list(product(range(1, N+1), repeat=M)):
    print(*i)