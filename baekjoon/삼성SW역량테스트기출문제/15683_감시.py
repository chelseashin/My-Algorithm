import sys
sys.stdin = open('15683_input.txt')

# 상 좌 하 우
dr = (-1, 0, 1, 0)
dc = (0, -1, 0, 1)

cctvDir = [
    [],
    [1, 0, 0, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 1],
    [1, 1, 1, 0],
    [1, 1, 1, 1]
]

def check(depth, dir):
    cnt = 0
    for i in range(4):
        if not dir[i]:
            continue
        r, c = cctv[depth]
        while True:
            r += dr[i]
            c += dc[i]
            if not (0 <= r < N and 0 <= c < M):
                break
            if S[r][c] == 6:
                break
            if S[r][c] == 0:
                S[r][c] = 10
                cnt += 1
            elif S[r][c] < 6:
                continue
            else:
                S[r][c] += depth
                continue
    return cnt

def clear(depth, dir):
    for i in range(4):
        if not dir[i]:
            continue
        r, c = cctv[depth]
        while True:
            r += dr[i]
            c += dc[i]
            if not (0 <= r < N and 0 <= c < M):
                break
            if S[r][c] == 6:
                break
            if S[r][c] == 10:
                S[r][c] = 0
                continue
            if S[r][c] > 10:
                S[r][c] -= depth
    return

def dfs(depth, total):
    global MIN
    if depth == K:
        MIN = min(MIN, space-total)
        return
    if space == total:
        MIN = 0
        return
    cctvNum = S[cctv[depth][0]][cctv[depth][1]]
    for i in range(4):
        newDir = cctvDir[cctvNum][i:4] + cctvDir[cctvNum][:i]
        count = check(depth, newDir)
        dfs(depth + 1, total + count)
        clear(depth, newDir)
        if cctvNum == 2 and i == 1:
            break
        if cctvNum == 5:
            break

# main
N, M = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(N)]
MIN = float('inf')

cctv = []
K = 0
space = 0
for i in range(N):
    for j in range(M):
        if S[i][j] and S[i][j] != 6:
            cctv.append((i, j))
            K += 1
        elif not S[i][j]:
            space += 1
dfs(0, 0)
print(MIN)