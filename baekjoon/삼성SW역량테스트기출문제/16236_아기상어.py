import sys
sys.stdin = open('16236_input.txt')

# 드디어 성공
# 참고 블로그 - 로직은 다르지만 푸는 방향 참고
# https://dailyheumsi.tistory.com/59

from collections import deque

# 상 좌 하 우
dr = (-1, 0, 1, 0)
dc = (0, -1, 0, 1)

def bfs(sr, sc):
    global eat, time, flag, shark_pos, shark
    visited = [[-1] * N for _ in range(N)]
    visited[sr][sc] = 0
    Q = deque([(sr, sc)])

    while Q:
        size = len(Q)
        Q = deque(sorted(Q))    # 상 > 좌 순으로 큐의 우선순위 정렬
        for _ in range(size):   # 꼭 필요한 작업. 현재 작업 수행할 때 큐에 새롭게 추가되는 값들과 구분해주기 위함
            r, c = Q.popleft()
            if S[r][c] and S[r][c] < shark:
                eat += 1
                if eat == shark:
                    shark += 1
                    eat = 0
                S[r][c] = 0
                flag = True
                shark_pos = [r, c]
                time += visited[r][c]
                return

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                if visited[nr][nc] >= 0:
                    continue
                if S[nr][nc] <= shark:
                    Q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1
    flag = False
    return

# main
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

# 1. 최초 상어의 위치, 해당 자리 비우기
shark_pos = []
for i in range(N):
    for j in range(N):
        if S[i][j] == 9:
            shark_pos = [i, j]      # 시작 상어 위치
            S[i][j] = 0

time = 0    # 시간 경과
shark = 2   # 현재 상어 크기
eat = 0     # 현재까지 먹은 물고기 수
flag = True     # 물고기 먹었는지 여부

# 2. 시작점에서 BFS 진행
while True:
    if not flag:    # 먹을 물고기 없으면 종료
        break
    bfs(shark_pos[0], shark_pos[1])

print(time)