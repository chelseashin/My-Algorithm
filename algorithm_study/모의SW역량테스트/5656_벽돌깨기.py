import copy
import sys
sys.stdin = open('5656_input.txt')

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dfs(depth, count):
    global total, N, B
    if total == result:
        return
    if depth == N or count == result:
        total = max(total, count)
        return
    for i in range(W):
        for j in range(H):
            if B[depth][j][i]:
                dfs(depth + 1, count + bomb(depth, j, i))
                break

def bomb(depth, sr, sc):
    global B, W, H
    bomb_count =0
    B[depth+1] = copy.deepcopy(B[depth])
    S = [(sr, sc)]
    while S:
        r, c = S.pop()
        power = B[depth+1][r][c]
        if power == 0:
            continue
        B[depth+1][r][c] = 0
        bomb_count += 1

        for i in range(4):
            for j in range(1, power):
                nr = r + dr[i] * j
                nc = c + dc[i] * j
                if not (0 <= nr < H and 0 <= nc < W):
                    break
                if B[depth+1][nr][nc] == 0:
                    continue
                S.append((nr, nc))
    down(depth+1)
    return bomb_count

def down(depth):
    global W, H
    remain = []
    for w in range(W):
        for h in range(H):
            if B[depth][h][w]:
                remain.append(B[depth][h][w])
        remain = [0] * (H - len(remain)) + remain
        for h in reversed(range(H)):
            B[depth][h][w] = remain.pop()

T = int(input())
for tc in range(T):
    N, W, H = map(int, input().split())
    B = [[[0] * W for _ in range(H)] for _ in range(N+1)]
    result = 0  # 전체 벽돌의 수
    total = 0   # 깬 벽돌의 수
    for i in range(H):
        B[0][i] = list(map(int, input().split()))
        result += sum(1 for j in B[0][i] if j)
    dfs(0, 0)

    print("#{} {}".format(tc + 1, result - total))

#1 12
#2 27
#3 4
#4 8
#5 0