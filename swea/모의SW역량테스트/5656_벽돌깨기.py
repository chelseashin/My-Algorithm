import sys
sys.stdin = open('5656_input.txt')

# 현재 무엇을 하고 있는지에 따라서 depth 계속 잘 따져주기

from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def gravity(depth):
    for c in range(W):
        remain = []
        for r in range(H):
            if raw_data[depth][r][c]:
                remain.append(raw_data[depth][r][c])
                raw_data[depth][r][c] = 0
        R = len(remain)
        for r in range(R):
            raw_data[depth][H-r-1][c] = remain.pop()


# bfs로 터트려야 할 좌표들 넣어주기
def bfs(sr, sc, depth):
    # 현재 depth에 작업하기 전에 전 depth의 결과를 복사해온다.
    raw_data[depth + 1] = [R[:] for R in raw_data[depth]]

    cnt = 0
    Q = deque([(sr, sc)])
    while Q:
        r, c = Q.popleft()
        power = raw_data[depth+1][r][c]
        if power == 0:
            continue
        raw_data[depth+1][r][c] = 0
        cnt += 1
        
        # 4방향 탐색하며 Q에 담기
        for dir in range(4):
            for p in range(1, power):
                nr = r + dr[dir] * p
                nc = c + dc[dir] * p
                if not (0 <= nr < H and 0 <= nc < W):
                    continue
                if not raw_data[depth+1][nr][nc]:
                    continue
                Q.append((nr, nc))

    gravity(depth+1)
    return cnt

def dfs(depth, total):
    global MIN
    if depth == N:
        MIN = min(MIN, brick-total)
        return
    if total == brick:
        MIN = 0
        return
    for c in range(W):
        for r in range(H):
            if raw_data[depth][r][c]:
                count = bfs(r, c, depth)
                dfs(depth+1, total+count)
                break

# main
T = int(input())
for tc in range(T):
    N, W, H = map(int, input().split())

    raw_data = [[[0] * W for _ in range(H)] for _ in range(N+1)]
    raw_data[0] = [list(map(int, input().split())) for _ in range(H)]

    brick = 0
    for i in range(H):
        for j in range(W):
            if raw_data[0][i][j]:
                brick += 1
    MIN = float('inf')

    dfs(0, 0)

    print('#{} {}'.format(tc+1, MIN))