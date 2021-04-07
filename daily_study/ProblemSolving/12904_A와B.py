# 23:38 start

from sys import stdin
input = stdin.readline

# def comb(depth, k, pick):
#     if depth == pick:
#         print(order)
#         return

#     for i in range(k, N):
#         order[i] = 1
#         comb(depth+1, i+1, pick)
#         order[i] = 0


def comb(depth, temp):
    if depth == N:
        if ''.join(temp) == str:
            print(order, ''.join(temp))
        return
    for i in range(2):
        order.append(i)
        # comb(depth+1, temp + ["A"])
        if i == 0:
            comb(depth+1, temp + ["A"])
        else:
            comb(depth+1, list(reversed(temp)) + ["B"])
        order.pop()

# main
S = list(input().rstrip())
T = list(input().rstrip())
N = len(T) - len(S)
L = "ABCDE"
print(S, T, N, "뒤집어", str(reversed(L)))

# order = [0] * N
# for i in range(N):
#     comb(0, 0, i)

order = []
comb(0, S)