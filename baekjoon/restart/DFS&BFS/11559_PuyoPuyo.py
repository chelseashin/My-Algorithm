import sys
sys.stdin = open('11559_input.txt')

# 같은 색 뿌요가 4개 이상 상하좌우로 연결되어 있으면 터짐
# 지워지고 떨어짐
# 연쇄반응 있음
# 터질 때마다 연쇄반응 cnt
# 동시반응은 연쇄 1로 침
# 알파벳은 색깔

from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 중력에 의해 아래로 떨어짐(행, 열 인덱스 잘 따지기)
def down():
    G = []
    for c in range(C):
        gravity = []
        dot = R
        for r in range(R-1, -1, -1):
            if puyopuyo[r][c] != '.':
                gravity.append(puyopuyo[r][c])
                dot -= 1
        gravity += ['.'] * dot
        G.append(gravity)
    # down 후 새로 맵 채워주기
    for i in range(C):
        for j in range(R):
            puyopuyo[R-j-1][i] = G[i][j]
    return

# 인접한 같은 색이 4개 이상이면 터트림
def bfs(sr, sc):
    global state
    visited = [[0] * C for _ in range(R)]
    color = [(sr, sc)]
    temp = puyopuyo[sr][sc]
    cnt = 1
    visited[sr][sc] = 1
    Q = deque([(sr, sc)])
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            if puyopuyo[nr][nc] == '.' or puyopuyo[nr][nc] != temp:
                continue
            if visited[nr][nc]:
                continue
            if puyopuyo[nr][nc] == temp and not visited[nr][nc]:   # 같은 색이면
                Q.append((nr, nc))
                cnt += 1
                visited[nr][nc] = 1
                color.append((nr, nc))
    # 4개 이상이면 터트리기
    if cnt >= 4:
        for i, j in color:
            puyopuyo[i][j] = '.'
        state += 1
    return

# main
R, C = 12, 6
puyopuyo = [list(input()) for _ in range(R)]

# 한 번에 터지는 것이 있는지를 더해줌
answer = 0
while True:
    state = 0
    for r in range(R):
        for c in range(C):
            if puyopuyo[r][c] != '.':
                bfs(r, c)
    down()
    # 터트린 게 있으면 연쇄반응한 것
    if state:
        answer += 1
    else:
        break
print(answer)