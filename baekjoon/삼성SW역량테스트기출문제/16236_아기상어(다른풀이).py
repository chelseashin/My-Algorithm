import sys
sys.stdin = open('16236_input.txt')

from collections import deque

# 상 좌 하 우
# dr = (-1, 0, 1, 0)
# dc = (0, -1, 0, 1)
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# main
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]


shark_pos = []
for i in range(N):
    for j in range(N):
        if S[i][j] == 9:
            shark_pos = [i, j]  # 시작 상어 위치
            S[i][j] = 0

size = 2    # 상어 크기
EXP = 0     # 상어 경험치
result = 0  # 이동 시간

while True:
    # 먹잇감 찾아내기(bfs)
    visited = [[0] * N for _ in range(N)]
    visited[shark_pos[0]][shark_pos[1]] = 1
    Q = deque()
    Q.append((*shark_pos, 0))
    # print(Q)

    fish = (N, N)
    min_dis = float('inf')
    while Q:
        r, c, cnt = Q.popleft()
        # 최소 거리보다 커지면 탐색 종료
        if cnt > min_dis:
            break

        # 우선순위에 따른 먹잇감 예약
        if S[r][c] and S[r][c] < size:
            if r < fish[0] or (r == fish[0] and c < fish[1]): # 상 좌 구역
                fish = (r, c)
                min_dis = cnt

        # 다음 탐색
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if visited[nr][nc]:
                continue
            if S[nr][nc] > size:
                continue
            visited[nr][nc] = 1
            Q.append((nr, nc, cnt+1))

    # 먹잇감 위치로 이동
    if fish == (N, N):  # 못 찾으면
        break
    else:
        S[fish[0]][fish[1]] = 0     # 물고기 제거
        shark_pos = (fish[0], fish[1])  # 상어 좌표 갱신
        EXP += 1
        if EXP == size:
            size += 1
            EXP = 0
        result += min_dis   # 이동거리 갱신

print(result)