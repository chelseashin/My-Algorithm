# Backtracking

import sys
input = sys.stdin.readline

# 가로 검사 - 해당 행에 값이 있는지 확인
def horizontal(row, value):
    if value in A[row]:
        return False
    return True

# 세로 검사 - 해당 열에 값이 있는지 확인
def vertical(col, value):
    for r in range(9):
        if A[r][col] == value:
            return False
    return True

def bythree(row, col, value):
    nr = row // 3 * 3
    nc = col // 3 * 3
    for i in range(3):
        for j in range(3):
            if value == A[nr+i][nc+j]:
                return False
    return True

def dfs(depth):
    if depth == zlen:
        for row in A:
            print(*row)
        exit()

    for i in range(1, 10):
        nr, nc = zeros[depth]
        # 가로, 세로, 3x3에 내가 대체하려는 숫자 존재하는지 확인
        if horizontal(nr, i) and vertical(nc, i) and bythree(nr, nc, i):
            A[nr][nc] = i
            dfs(depth+1)
            A[nr][nc] = 0

zeros = []
A = []
for i in range(9):
    A.append(list(map(int, input().split())))
    for j in range(9):
        if A[i][j] == 0:
            zeros.append((i, j))
zlen = len(zeros)
dfs(0)