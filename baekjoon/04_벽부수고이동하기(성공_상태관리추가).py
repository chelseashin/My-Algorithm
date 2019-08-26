import sys
sys.stdin = open('04_input.txt')

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def bfs(sr, sc):
    global arr, visited, N, M, Min
    # 행, 열, 폭탄의 수
    Q = [(sr, sc, 1)]
    visited[1][sr][sc] = 1
    # visited[0][sr][sc] = 1

    while Q:
        r, c, b = Q.pop(0)
        # if visited[b][r][c] > Min:
        #     return
        if r == N-1 and c == M-1:
            Min = visited[b][r][c]
            return
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if arr[nr][nc] == 1 and b == 1:
                if visited[0][nr][nc]:
                    continue
                visited[0][nr][nc] = visited[1][r][c] + 1
                Q.append((nr, nc, 0))
            elif arr[nr][nc] == 0:
                if visited[b][nr][nc]:
                    continue
                visited[b][nr][nc] = visited[b][r][c] + 1
                Q.append((nr, nc, b))


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
Min = float('inf')
visited =[[[0] * M for _ in range(N)] for _ in range(2)]
bfs(0, 0)

if Min == float('inf'):
    Min = -1
print(Min)