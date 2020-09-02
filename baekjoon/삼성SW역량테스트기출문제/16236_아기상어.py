import sys
sys.stdin = open('16236_input.txt')

from collections import deque

# 상 좌 하 우
dr = (-1, 0, 1, 0)
dc = (0, -1, 0, 1)

def bfs(sr, sc):
    global time, shark, count, shark_pos, flag
    visited = [[-1] * N for _ in range(N)]
    Q = deque([(sr, sc)])
    visited[sr][sc] = 0
    while Q:
        # Q = deque(sorted(Q))
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if visited[nr][nc] >= 0:
                continue
            if S[nr][nc] > shark:
                continue
            visited[nr][nc] = visited[r][c] + 1     # 거리 표시
            if S[nr][nc] < shark and S[nr][nc] > 0:
                count += 1
                shark_pos = [nr, nc]
                time += visited[nr][nc]
                S[nr][nc] = 0
                # fish -= 1
                print('상어 크기', shark, '먹은 수', count, shark_pos)
                if shark == count:
                    shark += 1      # 상어 크기 커짐
                    count = 0
                # for v in visited:
                #     print(v)
                flag = True
                return
            else:
                Q.append((nr, nc))
    flag = False
    return

# main
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]


shark_pos = []
for i in range(N):
    for j in range(N):
        if S[i][j] == 9:
            shark_pos = [i, j]  # 시작 상어 위치
            S[i][j] = 0

time = 0    # 시간 경과
shark = 2   # 현재 상어 크기
count = 0   # 상어가 먹은 물고기 수
flag = True
while True:
    if not flag:
        break
    pr, pc = shark_pos
    bfs(pr, pc)
    print(shark_pos, time, shark)
    # break

print('time', time)