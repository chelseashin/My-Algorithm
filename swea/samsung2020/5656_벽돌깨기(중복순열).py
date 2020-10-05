import sys
sys.stdin = open('5656_input.txt')
from collections import deque

# 상하좌우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def perm(depth):
    global cnt
    if depth == N:
        cnt += 1
        print(selected)
        return
    for i in range(W):
        selected[depth] = i
        perm(depth+1)
        selected[depth] = 0

# main
T = int(input())
for tc in range(T):
    N, W, H = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(H)]
    MIN = float('inf')
    print(N, W, H)
    # for r in raw:
    #     print(r)
    bricks = 0      # 맵에 있는 전체 벽돌의 수
    for h in range(H):
        for w in range(W):
            if raw[h][w]:
                bricks += 1
    cnt = 0
    selected = [0] * N
    perm(0)
    print(cnt)
    print("#{} {}".format(tc + 1, MIN))