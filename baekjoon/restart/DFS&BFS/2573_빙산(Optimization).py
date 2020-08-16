import sys
sys.stdin = open('2573_input.txt')

# copy 없이 sea에 녹인 정보 모두 표시
# 녹인 것이 0이면 -years-1로 표시해서
# 다음 녹일 것에 영향 가지 않도록 하기
# 0 부터 -years까지 모두 바다로 생각
# years 변수로 visited에 덮어쓰면서 표시
# 빙산 갯수 셀 때는 해당 변수인 것들로 세기

from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 빙산 몇 개인지 검사
def bfs(sr, sc):
    global years, visited
    Q = deque([(sr, sc)])
    visited[sr][sc] = years
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if sea[nr][nc] <= 0:
                continue
            if visited[nr][nc] == years:
                continue
            visited[nr][nc] = years
            Q.append((nr, nc))

# 빙산 녹이기
def melt():
    global sea, years
    for i in range(N):
        for j in range(M):
            if sea[i][j] > 0:
                temp = sea[i][j]
                zero = 0
                for dir in range(4):
                    nr = i + dr[dir]
                    nc = j + dc[dir]
                    if not (0 <= nr < N and 0 <= nc < M):
                        continue
                    if (-years-1) < sea[nr][nc] <= 0:
                        zero += 1
                if zero:
                    if temp - zero > 0:
                        sea[i][j] = temp - zero
                    else:
                        sea[i][j] = -years-1

# main
N, M = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(N)]

years = 0
visited = [[0] * M for _ in range(N)]
while True:
    # 녹이고 1년 후
    melt()
    years += 1
    # 빙산 몇 개인지 검사
    iceberg = 0
    for i in range(N):
        for j in range(M):
            if sea[i][j] > 0 and visited[i][j] != years:
                bfs(i, j)
                iceberg += 1
            # 빙산 2개 이상이면 break
            if iceberg == 2:
                break
    # 종료조건은 빙산이 아예 없어지거나 2개 이상일 때
    if iceberg == 0:
        print(0)
        break
    if iceberg >= 2:
        print(years)
        break