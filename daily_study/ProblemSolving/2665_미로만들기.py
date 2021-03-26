from sys import stdin
input = stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs():
    visited = [[float('inf')] * N for _ in range(N)]    # 최댓값으로 초기화
    visited[0][0] = 0
    Q = deque([(0, 0, 0)])
    while Q:
        r, c, cnt = Q.popleft()
        if (r, c) == (N-1, N-1):
            print(cnt)
            return
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < N and 0 <= nc < N):   # 격자 밖으로 나가면
                continue

            # 이동할 곳이 흰 방일 때 최솟값으로 갱신할 수 있는 곳일 때만 값 갱신
            if maze[nr][nc] == '1' and visited[nr][nc] > visited[r][c]:
                visited[nr][nc] = cnt
                Q.appendleft((nr, nc, cnt))

            # 이동할 곳이 검은 방일 때
            if maze[nr][nc] == '0':
                # 이미 방문했다면 최솟값으로 갱신할 수 있는 곳일 때만 값 갱신
                if visited[nr][nc] != float('inf') and visited[r][c] + 1 < visited[nr][nc]:
                    visited[nr][nc] = cnt + 1
                    Q.append((nr, nc, cnt + 1))
                # 아직 방문하지 않았다면 첫 방문이므로 검은 방을 흰 방으로 갱신
                if visited[nr][nc] == float('inf'):
                    visited[nr][nc] = cnt + 1
                    Q.append((nr, nc, cnt + 1))

# main
N = int(input())
maze = [list(input().strip()) for _ in range(N)]
bfs()