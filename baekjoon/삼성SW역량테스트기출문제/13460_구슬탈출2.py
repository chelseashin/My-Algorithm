# 1. 빨간 구슬과 파란 구슬을 기울인 방향에 대해서 갈 수 있는 만큼 이동했을 때의 좌표를 구함
# 2. 중간에 파란 구슬이 구멍에 빠지면 continue하여 다른 방향으로 기울인 경우로 넘어감
# 3. 빨간 구슬과 파란 구슬이 겹치면 각각 이동한 길이를 구하여 앞뒤로 위치하도록 처리
# 4. 방문한 적이 없다면 방문 체크 해주기
# 5. 빨간 구슬이 빠지면 기울인 횟수를 출력하고 10번 넘어가면 -1 출력

import sys
sys.stdin = open('13460_input.txt')
input = sys.stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs(rr, rc, br, bc, cnt):
    Q = deque([(rr, rc, br, bc)])
    visited = [(rr, rc, br, bc)]
    while Q:
        qlen = len(Q)
        if cnt > 10:
            print(-1)
            return
        while qlen:
            rr, rc, br, bc = Q.popleft()
            # 빨간 구슬이 구멍에 빠지면
            if B[rr][rc] == 'O':
                print(cnt)
                return
            # 기울이기
            for d in range(4):
                nrr, nrc, nbr, nbc = rr, rc, br, bc
                # 빨간 구슬
                while True:
                    nrr += dr[d]
                    nrc += dc[d]
                    if B[nrr][nrc] == "O":
                        break
                    if B[nrr][nrc] == "#":
                        nrr -= dr[d]
                        nrc -= dc[d]
                        break
                # 파란 구슬
                while True:
                    nbr += dr[d]
                    nbc += dc[d]
                    if B[nbr][nbc] == "O":
                        break
                    if B[nbr][nbc] == "#":
                        nbr -= dr[d]
                        nbc -= dc[d]
                        break
                # 파란 구슬이 구멍에 빠지면 실패 -> 계속
                if B[nbr][nbc] == "O":
                    continue
                # 두 구슬이 같은 위치일 때
                if nrr == nbr and nrc == nbc:
                    # 빨간 구슬의 이동 길이가 더 길면
                    if abs(rr-nrr) + abs(rc-nrc) > abs(br-nbr) + abs(bc-nbc):
                        nrr -= dr[d]
                        nrc -= dc[d]
                    else:   # 파란 구슬의 이동 길이가 더 길면
                        nbr -= dr[d]
                        nbc -= dc[d]

                if (nrr, nrc, nbr, nbc) not in visited:
                    visited.append((nrr, nrc, nbr, nbc))
                    Q.append((nrr, nrc, nbr, nbc))
            qlen -= 1
        cnt += 1
    print(-1)
    return


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

bfs(rr, rc, br, bc, 0)