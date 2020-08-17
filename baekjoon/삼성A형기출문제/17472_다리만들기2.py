import sys
sys.stdin = open('17472_input.txt')

# 다시 풀어보세요!

# 제한
# 1 ≤ N, M ≤ 10
# 3 ≤ N×M ≤ 100
# 2 ≤ 섬의 개수 ≤ 6

from collections import deque

# 상하좌우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# main
N, M = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(N)]
print(sea)
