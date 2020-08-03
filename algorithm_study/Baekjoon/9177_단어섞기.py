import sys
sys.stdin = open('9177_input.txt')

from itertools import combinations

T = int(input())
for tc in range(T):
    A, B, C = map(str, input().split())

    print(A, B, C)
    # print(L)