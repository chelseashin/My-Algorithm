# 정답 코드 - 매우 깔끔..

from sys import stdin
input = stdin.readline

M, N = map(int, input().split())
order = [1] * (2*M-1)
for _ in range(N):
    zero, one, two = map(int, input().split())
    for i in range(zero, zero+one):
        order[i] += 1
    for i in range(zero+one, len(order)):
        order[i] += 2
# print(order)

for r in range(M):
    for c in range(M):
        if c == 0:
            print(order[M-1-r], end=" ")
        else:
            print(order[M+c-1], end=" ")
    print()