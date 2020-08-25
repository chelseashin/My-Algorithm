import sys
sys.stdin = open('5656_input.txt')

# 실패.. 꼭 다시 풀기!

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bomb(r, c, dir, power, Q):
    for p in range(1, power):
        nr = r + dr[dir] * p
        nc = c + dc[dir] * p
        if not (0 <= nr < H and 0 <= nc < W):
            continue
        if raw[nr][nc]:
            Q.append((nr, nc, raw[nr][nc]))
            raw[nr][nc] = 0


# bfs로 터트려야 할 좌표들 넣어주기
def bfs(sr, sc):
    Q = deque([(sr, sc, raw[sr][sc])])
    cnt = 0
    while Q:
        r, c, p = Q.popleft()
        raw[r][c] = 0
        cnt += 1
        for d in range(4):
            bomb(r, c, d, p, Q)
    # print(cnt)
    return cnt
    # down()

def dfs(depth, total):
    global MIN
    if depth == N:
        MIN = min(MIN, brick-total)
        # print('MIN', MIN)
        return
    for c in range(W):
        for r in range(H):
            if raw[r][c]:
                count = bfs(r, c)
                print('count', count)
                dfs(depth+1, total+count)
            # break
            dfs(depth+1, total)


# main
T = int(input())
for tc in range(T):
    N, W, H = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(H)]
    print(raw)
    MIN = float('inf')

    brick = 0
    for i in range(H):
        for j in range(W):
            if raw[i][j]:
                brick += 1
    # print(brick)

    dfs(0, 0)

    print('#{} {}'.format(tc+1, MIN))