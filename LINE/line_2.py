import sys
sys.stdin = open('line_2.txt')

import itertools

L = sorted(list(map(int, input().strip().split(' '))))
N = int(input())
# print(list(itertools.permutations(L, 3)))
P = list(itertools.permutations(L, 3))
print(P)
p = P[N-1]

answer = ''
for i in range(len(L)):
    answer += str(p[i])

print(answer)