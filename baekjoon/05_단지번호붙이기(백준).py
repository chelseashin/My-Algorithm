import sys
sys.stdin = open('05_input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(sr, sc):
    global arr, visited, N, L, count
    S = [(sr, sc)]
    visited[sr][sc] = 1
    num = 1
    cnt = 1
    while S:
        r, c = S.pop()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if arr[nr][nc] == 0:
                continue
            if visited[nr][nc]:
                continue
            S.append((nr, nc))
            visited[nr][nc] = num
            cnt += 1
    num += 1
    L.append(cnt)

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
L = []
count = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            dfs(i, j)
            count += 1

print(count)
for i in sorted(L):
    print(i)