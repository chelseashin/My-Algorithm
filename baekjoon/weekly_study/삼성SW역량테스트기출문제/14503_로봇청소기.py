import sys
sys.stdin = open("14503_input.txt")
input = sys.stdin.readline

# 북 동 남 서
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

# main
N, M = map(int, input().split())
r, c, d = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
print(N, M, r, c, d)
cnt = 0

# for a in A:
#     print(a)
#
# for v in visited:
#     print(v)