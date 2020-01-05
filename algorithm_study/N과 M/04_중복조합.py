import sys
sys.stdin = open("input.txt")

# 중복조합 공식
def comb(depth, k):
    global N, M
    if depth == M:
        print(*order)
        return
    for i in range(k, N+1):
        order.append(i)
        comb(depth+1, i)
        order.pop()


N, M = map(int, input().split())
order = []
comb(0, 1)