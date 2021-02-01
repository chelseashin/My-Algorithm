# 9:45 start
# 10:50 finish
# 1h 5m

import sys
input = sys.stdin.readline
from collections import deque

# 4방향
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def puyopuyo():
    global flag, puyo
    for sr in range(R):
        for sc in range(C):
            if A[sr][sc] != '.':
                temp = A[sr][sc]        # 현재 값
                Q = deque([(sr, sc)])
                check = {(sr, sc)}      # 방문 여부 set으로 관리
                while Q:
                    r, c = Q.popleft()
                    for d in range(4):
                        nr = r + dr[d]
                        nc = c + dc[d]
                        if not (0 <= nr < R and 0 <= nc < C):
                            continue
                        if A[r][c] == "." or (nr, nc) in check:
                            continue
                        if A[nr][nc] == temp:   # 같은 값이면
                            Q.append((nr, nc))
                            check.add((nr, nc))
                if len(check) >= 4:
                    flag = True         # 4개 이상이면 True
                    for r, c in check:
                        A[r][c] = "."   # 뿌요 터트리기
                        puyo -= 1

def down():
    for j in range(C):
        q = deque()         # 열에 남은 뿌요
        for i in range(R):
            if A[i][j] != ".":
                q.appendleft(A[i][j])
                A[i][j] = "."
        row = R-1
        while q:
            A[row][j] = q.popleft()
            row -= 1

# main
R, C = 12, 6
puyo = 0
A = []
for row in range(R):
    A.append(list(input().strip()))
    for col in range(C):
        if A[row][col] != ".":
            puyo += 1

turn = 0        # 몇 연쇄인지
while True:
    flag = False    # 이번 턴에 터트렸는지
    puyopuyo()
    if flag:        # 터뜨렸으면
        turn += 1
        if not puyo:
            break
        down()  # 뿌요 아래로 내리기
    else:
        break
print(turn)