import sys
sys.stdin = open('2573_input.txt')
from collections import deque
input = sys.stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs(sr, sc):
    check[sr][sc] = time
    Q = deque([(sr, sc)])
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if iceburg[nr][nc] and check[nr][nc] != time:
                Q.append((nr, nc))
                check[nr][nc] = time

# main
N, M = map(int, input().split())
iceburg = [list(map(int, input().split())) for _ in range(N)]
time = 0
check = [[0] * M for _ in range(N)]
while True:
    time += 1
    # 빙산 녹은 양 표시
    visited = [[0] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if iceburg[r][c]:
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if not (0 <= nr < N and 0 <= nc < M):
                        continue
                    if iceburg[nr][nc] == 0:
                        visited[r][c] += 1

    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                iceburg[i][j] -= visited[i][j]
                if iceburg[i][j] < 0:
                    iceburg[i][j] = 0

    cnt = 0    # 빙산의 갯수 세기
    for i in range(N):
        for j in range(M):
            # 전역변수 check 배열 재활용 => 시간으로 구분
            if iceburg[i][j] and check[i][j] != time:
                bfs(i, j)
                cnt += 1
            if cnt >= 2:
                break

    if cnt == 0:
        print(0)
        break
    if cnt >= 2:
        print(time)
        break