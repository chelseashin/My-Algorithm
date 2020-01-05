import sys
sys.stdin = open("input.txt")

# 조합공식
def comb(depth, k):
    global N, M
    if depth == M:
        print(*order)
        return
    for i in range(k, N+1):
        order.append(i)
        comb(depth+1, i+1)
        order.pop()


N, M = map(int, input().split())
order = []
comb(0, 1)