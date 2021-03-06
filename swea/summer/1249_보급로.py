import sys
sys.stdin = open("1249_input.txt")

# 상 하 좌 우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs(sr, sc):
    global arr, N, visited
    Q = [(sr, sc)]
    visited[sr][sc] = 0
    while Q:
        r, c = Q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            time = arr[nr][nc]
            if visited[nr][nc] > visited[r][c] + time:
                visited[nr][nc] = visited[r][c] + time
                Q.append((nr, nc))

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[float('inf')] * N for _ in range(N)]
    bfs(0, 0)
    print("#{} {}".format(tc+1, visited[N-1][N-1]))

# 2
# dx = (-1, 1, 0, 0)
# dy = (0, 0, -1, 1)
#
# def dfs():
#     V[0][0] = A[0][0]
#     q = [[0, 0]]
#
#     while q:
#         a = q.pop(0)
#         y, x = a[0], a[1]
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if not (0 <= nx < N and 0 <= ny < N):
#                 continue
#             if V[ny][nx] > V[y][x] + A[ny][nx]:
#                 V[ny][nx] = V[y][x] + A[ny][nx]
#                 q.append([ny, nx])
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     A = [list(map(int, (input()))) for i in range(N)]
#     V = [[100000] * N for i in range(N)]
#     dfs()
#
#     print("#{} {}".format(tc, V[N - 1][N - 1]))
