import sys
sys.stdin = open("input2.txt")

def comb(depth, k):
    global N, M
    if depth == M:
        print(*order)
        return
    for i in range(k, len(A)):
        order.append(A[i])
        comb(depth+1, i)
        order.pop()
#
N, M = map(int, input().split())
A = sorted(list(set(list(map(int, input().split())))))
order = []
comb(0, 0)
