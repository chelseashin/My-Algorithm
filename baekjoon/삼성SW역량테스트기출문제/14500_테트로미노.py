import sys
sys.stdin = open('14500_input.txt')

# dr = (-1, 1, 0, 0)
# dc = (0, 0, -1, 1)

jr = (-1, 1, 0, 0, -1, -1, 1, 1)
jc = (0, 0, -1, 1, -1, 1, -1, 1)

dr = (1, 0)
dc = (0, 1)

def dfs(depth, r, c):
    global cnt, MAX
    if depth == 3:
        cnt += 1
        print(visited)
        temp = 0
        for i in range(N):
            for j in range(M):
                if visited[i][j]:
                    temp += A[i][j]
        # print(temp)
        MAX = max(MAX, temp)
        return
    if depth == 2:
        for j in range(8):
            nr_ = r + jr[j]
            nc_ = c + jc[j]
            if not (0 <= nr_ < N and 0 <= nc_ < M):
                continue
            if visited[nr_][nc_]:
                continue
            visited[nr_][nc_] = 1
            dfs(depth + 1, nc_, nc_)
            visited[nr_][nc_] = 0

    for i in range(2):
        nr = r + dr[i]
        nc = c + dc[i]
        if not (0 <= nr < N and 0 <= nc < M):
            continue
        if visited[nr][nc]:
            continue
        visited[nr][nc] = 1
        dfs(depth+1, nr, nc)
        visited[nr][nc] = 0

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
# print(A)
MAX = float('-inf')
cnt = 0
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(0, i, j)
        visited[i][j] = 0
print(cnt)
print(MAX)