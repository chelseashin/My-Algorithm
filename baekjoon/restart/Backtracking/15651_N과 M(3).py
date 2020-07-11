N, M = 4, 2
# N, M = map(int, input().split())

def perm(depth):
    if depth == M:
        print(*order)
        return
    for i in range(1, N+1):
        order.append(i)
        perm(depth+1)
        order.pop()

order = []
perm(0)

# 시간, 메모리 더 많이 걸림
# from itertools import product
# for i in list(product(range(1, N+1), repeat=M)):
#     print(*i)