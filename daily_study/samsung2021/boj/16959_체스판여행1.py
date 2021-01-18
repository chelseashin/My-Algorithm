#
# h m

import sys
input = sys.stdin.readline

knight_dr = (-1, -1, -2, -2, 2, 2, 1, 1)
knight_dc = (-2, 2, -1, 1, -1, 1, -2, 2)

# 대각선이라면 어디든. 기물 뛰어넘을 수 X
rook_dr = (0, 0, 1, -1)
rook_dc = (1, -1, 0, 0)

# 직선이라면 어디든. 기물 뛰어넘을 수 X
bishop_dr = (1, -1, 1, -1)
bishop_dc = (1, -1, -1, 1)

# main
N = int(input())
D = dict()
raw = [list(map(int, input().split())) for _ in range(N)]
print(raw)


