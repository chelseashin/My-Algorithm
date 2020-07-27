import sys
sys.stdin = open('19_input.txt')

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dfs(sr, sc):
    global color, visited, temp
    S = [(sr, sc)]
    while S:
        r, c = S.pop()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if visited[nr][nc]:
                continue
            if color[nr][nc] == temp:
                visited[nr][nc] = 1
                S.append((nr, nc))

def dfs2(sr, sc):
    global rg_color, visited, temp
    S = [(sr, sc)]
    while S:
        r, c = S.pop()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if visited[nr][nc]:
                continue
            if rg_color[nr][nc] == temp:
                visited[nr][nc] = 1
                S.append((nr, nc))

N = int(input())
arr = list(input() for _ in range(N))
color = [[0] * N  for _ in range(N)]
rg_color = [[0] * N  for _ in range(N)]
visited = [[0] * N  for _ in range(N)]

for i in range(N):
    for j in range(N):
        color[i][j] = arr[i][j]
        if arr[i][j] == 'G':
            rg_color[i][j] = 'R'
            continue
        rg_color[i][j] = arr[i][j]

visited = [[0] * N  for _ in range(N)]
cnt1 = 0
for i in range(N):
    for j in range(N):
        if color[i][j] and visited[i][j] == 0:
            temp = color[i][j]
            dfs(i, j)
            cnt1 += 1

visited = [[0] * N  for _ in range(N)]
cnt2 = 0
for i in range(N):
    for j in range(N):
        if rg_color[i][j] and visited[i][j] == 0:
            temp = rg_color[i][j]
            dfs2(i, j)
            cnt2 += 1

print(cnt1, cnt2)