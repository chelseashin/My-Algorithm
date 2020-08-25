import sys
sys.stdin = open('5656_input.txt')

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dfs(S):
    cnt = 0
    while S:
        d, r, c = S.pop()
        size = data[d][r][c]
        if data[d][r][c]:
            cnt += 1
        data[d][r][c] = 0
        for dis in range(1, size):
            for i in range(4):
                nr = r + dr[i] * dis
                nc = c + dc[i] * dis
                if not (0 <= nr < H and 0 <= nc < W):
                    continue
                if not data[d][nr][nc]:
                    continue
                S.append((d, nr, nc))
    return cnt

# 문제 없음
def cpy(depth):
    for i in range(H):
        if depth == 0:
            data[0][i] = raw[i][:]
        else:
            data[depth][i] = data[depth-1][i][:]

# 구슬 쏜 횟수, 벽돌 깬 갯수
def start(depth, total):
    global result, brick
    stack = []
    # 구슬 N번 모두 쏘거나, 벽돌 다 깼을 경우
    if depth == N or total == brick:
        result = max(total, result)
        return
    # print(data)
    for col in range(W):
        cpy(depth)
        # print(data)
        for row in range(H):
            if data[depth][row][col]:
                stack.append((depth, row, col))
                cnt = dfs(stack)
                # print(cnt)
                break
        else:
            continue
        gravity(depth)
        start(depth + 1, total + cnt)

def gravity(depth):
    for col in range(W):
        for row in range(H-1, 0, -1):
            if data[depth][row][col] == 0:
                for row2 in range(row-1, -1, -1):
                    if data[depth][row2][col]:
                        data[depth][row][col], data[depth][row2][col] = data[depth][row2][col], data[depth][row][col]
                        break
# main
T = int(input())
for tc in range(T):
    N, W, H = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(H)]
    # print(raw)
    data = [[[0] * W for _ in range(H)] for _ in range(N)]

    brick = 0
    for i in range(H):
        for j in range(W):
            if raw[i][j]:
                brick += 1

    result = 0
    start(0, 0)
    print("#{} {}".format(tc+1, brick-result))

    # 1 12
    # 2 27
    # 3 4
    # 4 8
    # 5 0