import sys
sys.stdin = open('5656_input.txt')
from collections import deque

# 상하좌우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# main
T = int(input())
for tc in range(T):
    N, W, H = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    MIN = float('inf')
    print(N, W, H)
    print("#{} {}".format(tc+1, MIN))