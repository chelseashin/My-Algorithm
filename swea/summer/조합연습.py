from itertools import combinations


print(list(combinations(range(1, 5), 2)))

N, M = 4, 2
# N, M = map(int, input().split())
# for x in list(combinations(range(1, N+1), M)):
#     print(*x)

def comb(depth, k):
    global N, M
    if depth == M:
        print(*order)
        return
    for i in range(k, N+1):
        order.append(i)
        comb(depth+1, i+1)
        order.pop()

order = []
comb(0, 1)