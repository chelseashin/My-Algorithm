import sys
sys.stdin = open("3187_input.txt")

from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs(sr, sc):
    visited[sr][sc] = 1
    Q = deque([(sr, sc)])
    V, K = 0, 0     # 늑대 'v', 양 'k'

    return

# main
R, C = map(int, input().split())
A = [list(input()) for _ in range(R)]
for a in A:
    print(a)

wolf, sheep = 0, 0
visited = [[0] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if visited[i][j] and A[i][j] != "#":
            v, k = bfs(i, j)
            wolf += v
            sheep += k

print(sheep, wolf)