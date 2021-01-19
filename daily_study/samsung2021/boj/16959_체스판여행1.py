#
# h m
# 1. 맵에 대한 정보를 넣는다
# 2. 나이트는 총 8방향, 룩은 십자가 방향으로 이동, 비숍은 대각선 방향으로 이동
#    이 때, 말은 다른 수 적힌 칸 방문할 수 있음.
# 3. 1초에 할 수 있는 일은 1. 말을 바꾸거나 2. 기존 말로 이동
# 4. visited 배열을 [x][y][종류][번호]로 해서 이동을 할 때
#    다음 번호가 아니면 계속 이전 번호로 처리해야 한다

import sys
input = sys.stdin.readline
from collections import deque



dd = [[[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]],
       [[-1, -1], [-1, 1], [1, -1], [1, 1]],
       [[1, 0], [-1, 0], [0, 1], [0, -1]]]

# main
N = int(input())
raw = []
visited = [[[0] * 3 for _ in range(N)] for _ in range(N)]
Q = deque()
for i in range(N):
    raw.append(list(map(int, input().split())))
    for j in range(N):
        if raw[i][j] == 1:      # 1이 있는 칸에
            for k in range(3):  # 나이트, 룩, 비숍 중 하나를 놓으며 시작
                visited[i][j][k] = 1
                Q.append((i, j, k, 1))

result, cnt, goal = -1, 0, N*N
while Q and result == -1:
    qlen = len(Q)
    for k in range(qlen):
        r, c, p, temp = Q.popleft()
        if temp == goal:
            result = cnt
            # print(cnt)
            break
        for x in range(3):      # 말 3개
            if temp > visited[r][c][x]:
                visited[r][c][x] = temp
                Q.append((r, c, x, temp))

        for dr, dc in dd[p]:
            nr = r + dr
            nc = c + dc
            while (0 <= nr < N and 0 <= nc < N):
                if temp > visited[nr][nc][p]:
                    nexttemp = temp + (raw[nr][nc] == temp+1)
                    visited[nr][nc][p] = nexttemp
                    Q.append((nr, nc, p, nexttemp))
                nr += dr
                nc += dc
                if p == 0:  # 나이트면 나가기
                    break
    cnt += 1
print(result)
# for v in visited:
#     print(v)
