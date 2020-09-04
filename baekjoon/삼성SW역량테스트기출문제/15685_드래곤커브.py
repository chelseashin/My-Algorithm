import sys
sys.stdin = open('15685_input.txt')

# 우, 상, 좌, 하
dr = (0, -1, 0, 1)
dc = (1, 0, -1, 0)


N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]

print(info)

for curve in info:
    r, c, d, g = curve
