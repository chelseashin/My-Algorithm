# 15:55 start
# 16:23

import sys
input = sys.stdin.readline

# 방법 1
def comb(depth, k, temp):
    if depth == L:
        vowel = 0
        for s in temp:
            if s in "aeiou":
                vowel += 1
        if vowel >= 1 and L-vowel >= 2:
            print(temp)
        return
    for i in range(k, C):
        comb(depth+1, i+1, temp + A[i])

# main
L, C = map(int, input().split())
A = sorted(list(input().split()))
comb(0, 0, "")

# 방법 2
# from itertools import combinations
#
# vowel = set("aeiou")
# for comb in combinations(A, L):
#     set_comb = set(comb)
#     if set_comb & vowel and len(set_comb - vowel) >= 2:
#         print(''.join(comb))