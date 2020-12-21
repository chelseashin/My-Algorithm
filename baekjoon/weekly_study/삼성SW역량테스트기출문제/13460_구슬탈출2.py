import sys
sys.stdin = open("13460_input.txt")
input = sys.stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def move(r, c, dr, dc):
    temp = 0
    while board[r+dr][c+dc] != "#" and board[r][c] != "O":
        r += dr
        c += dc
        temp += 1
    return r, c, temp

def bfs(rr, rc, br, bc):
    visited = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    visited[rr][rc][br][bc] = 1
    Q = deque([(rr, rc, br, bc, 0)])
    while Q:
        rr, rc, br, bc, cnt = Q.popleft()
        if cnt > 10:
            return -1
        for i in range(4):
            # move 함수 : 좌표, 방향 넘겨주면 이동 후 좌표와 움직인 칸 수 리턴
            nrr, nrc, rcnt = move(rr, rc, dr[i], dc[i])
            nbr, nbc, bcnt = move(br, bc, dr[i], dc[i])
            # 파란 구슬이 구멍에 빠지면
            if board[nbr][nbc] == "O":
                continue
            # 빨간 구슬이 구멍에 빠지면
            if board[nrr][nrc] == "O":
                return cnt + 1
            # 이동 후 같은 위치라면 이동 거리가 긴 구슬을 한 칸 전으로 옮기기
            if nrr == nbr and nrc == nbc:
                if rcnt > bcnt:
                    nrr -= dr[i]
                    nrc -= dc[i]
                else:
                    nbr -= dr[i]
                    nbc -= dc[i]
            if not visited[nrr][nrc][nbr][nbc]:
                visited[nrr][nrc][nbr][nbc] = 1
                Q.append((nrr, nrc, nbr, nbc, cnt+1))
    return -1

# main
N, M = map(int, input().split())
board = []
rr, rc = 0, 0
br, bc = 0, 0
for i in range(N):
    board.append(list(input().strip()))
    for j in range(M):
        if board[i][j] == "R":
            rr, rc = i, j
            board[i][j] = "."
        elif board[i][j] == "B":
            br, bc = i, j
            board[i][j] = "."

# for b in board:
#     print(b)
# print((rr, rc), (br, bc))

print((bfs(rr, rc, br, bc)))