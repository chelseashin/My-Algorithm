import sys
sys.stdin = open('13460_input.txt')
input = sys.stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 기울이기
def move(r, c, dr, dc):
    cnt = 0
    while True:
        nr = r + dr
        nc = c + dc
        cnt += 1
        if B[nr][nc] == "O":        # 구멍에 빠지면 그 칸
            return (nr, nc, cnt)
        elif B[nr][nc] == "#":      # 벽에 닿으면 그 전 칸
            return (r, c, cnt-1)
        r, c = nr, nc

def bfs(rr, rc, br, bc):
    visited = [[[[-1] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    visited[rr][rc][br][bc] = 0
    Q = deque([(rr, rc, br, bc)])
    while Q:
        rr, rc, br, bc = Q.popleft()
        if visited[rr][rc][br][bc] > 10:
            break
        # 빨간 구슬이 구멍에 빠지면 끝
        if B[rr][rc] == "O":
            return visited[rr][rc][br][bc]
        # 4방향 기울이기
        for d in range(4):
            nrr, nrc, nrd = move(rr, rc, dr[d], dc[d])
            nbr, nbc, nbd = move(br, bc, dr[d], dc[d])
            # 파란 구슬 구멍에 빠지면 다른 방향으로 기울이기
            if B[nbr][nbc] == "O":
                continue
            # 두 구슬 겹치면 이동 거리 긴 구슬을 한칸 뒤로
            if nrr == nbr and nrc == nbc:
                if nrd > nbd:
                    nrr -= dr[d]
                    nrc -= dc[d]
                else:
                    nbr -= dr[d]
                    nbc -= dc[d]
            # 방문 검사
            if visited[nrr][nrc][nbr][nbc] != -1:
                continue
            visited[nrr][nrc][nbr][nbc] = visited[rr][rc][br][bc] + 1
            Q.append((nrr, nrc, nbr, nbc))
    return -1

# main
N, M = map(int, input().split())
B = [list(input()) for _ in range(N)]

rr, rc = 0, 0
br, bc = 0, 0
for i in range(N):
    for j in range(M):
        if B[i][j] == "R":
            rr, rc = i, j
        elif B[i][j] == "B":
            br, bc = i, j

print(bfs(rr, rc, br, bc))