import sys
sys.stdin = open("13460_input.txt")
input = sys.stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs(rr, rc, br, bc):
    Q = deque([(rr, rc, br, bc)])
    visited = [(rr, rc, br, bc)]
    cnt = 0
    while Q:
        cnt += 1
        if cnt > 10:
            print(-1)
            return
        qlen = len(Q)
        for _ in range(qlen):
            rr, rc, br, bc = Q.popleft()
            for d in range(4):
                nrr, nrc, nbr, nbc = rr, rc, br, bc
                # 빨간 구슬 움직이기
                rcnt = 0
                while True:
                    nrr += dr[d]
                    nrc += dc[d]
                    if board[nrr][nrc] == "O":
                        break
                    if board[nrr][nrc] == "#":
                        nrr -= dr[d]
                        nrc -= dc[d]
                        break
                    rcnt += 1
                # 파란 구슬 움직이기
                bcnt = 0
                while True:
                    nbr += dr[d]
                    nbc += dc[d]
                    if board[nbr][nbc] == "O":
                        break
                    if board[nbr][nbc] == "#":
                        nbr -= dr[d]
                        nbc -= dc[d]
                        break
                    bcnt += 1
                # 파란 구슬 구멍에 빠지면 계속
                if board[nbr][nbc] == "O":
                    continue
                # 빨간 구슬 구멍에 빠지면 리턴
                if board[nrr][nrc] == "O":
                    print(cnt)
                    return
                # 두 구슬이 같은 위치라면 이동거리 긴 구슬이 한칸 전 칸으로 이동
                if nrr == nbr and nrc == nbc:
                    if rcnt > bcnt:
                        nrr -= dr[d]
                        nrc -= dc[d]
                    else:
                        nbr -= dr[d]
                        nbc -= dc[d]
                if (nrr, nrc, nbr, nbc) not in visited:
                    visited.append((nrr, nrc, nbr, nbc))
                    Q.append((nrr, nrc, nbr, nbc))
    print(-1)
    return


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

bfs(rr, rc, br, bc)