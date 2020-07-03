import sys
sys.stdin = open("1953_input.txt")

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

IN = [[1, 2, 5, 6], [1, 2, 4, 7], [1, 3, 4, 5], [1, 3, 6, 7]]
OUT = [[1, 2, 4, 7], [1, 2, 5, 6], [1, 3, 6, 7], [1, 3, 4, 5]]

def bfs(sr, sc):
    global N, M, L, cnt
    Q = [(sr, sc)]
    visited[sr][sc] = 1
    while Q:
        r, c = Q.pop(0)
        cnt += 1
        for i in range(4):
            if info[r][c] not in OUT[i]:
                continue
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if info[nr][nc] == 0:
                continue
            if info[nr][nc] in IN[i] and visited[nr][nc] == 0:
                visited[nr][nc] = visited[r][c] + 1
                if visited[nr][nc] <= L:
                    Q.append((nr, nc))

T = int(input())
for tc in range(T):
    N, M, R, C, L = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    cnt = 0
    bfs(R, C)
    # print(visited)
    print("#{} {}".format(tc+1, cnt))