import sys
sys.stdin = open('05_input.txt')

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs(sr, sc):
    global visited, arr, N
    cnt = 1
    Q = [(sr, sc)]
    visited[sr][sc] = 1
    while Q:
        r, c = Q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if visited[nr][nc]:
                continue
            if arr[nr][nc] == 0:
                continue
            Q.append((nr, nc))
            visited[nr][nc] = 1
            cnt += 1
    L.append(cnt)
    return


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
L = []
for i in range(N):
    for j in range(N):
        if arr[i][j] and visited[i][j] == 0:
            bfs(i, j)

print(len(L))
for i in sorted(L):
    print(i)

# print(visited)