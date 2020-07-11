import sys
sys.stdin = open('2580_input.txt')

# 가로 체크
def garo(r, value):
    if value in sudoku[r]:
        return 0
    return 1

# 세로 체크
def sero(c, value):
    for i in range(9):
        if value == sudoku[i][c]:
            return 0
    return 1

# 3 X 3 체크
def bythree(r, c, value):
    nr = r//3 * 3
    nc = c//3 * 3
    for i in range(3):
        for j in range(3):
            if value == sudoku[nr+i][nc+j]:
                return 0
    return 1


def dfs(depth):
    if depth == len(zeros):
        for row in sudoku:
            print(*row)
        return

    # 1부터 9까지 숫자 모두 넣어보기
    for i in range(1, 10):
        nr = zeros[depth][0]
        nc = zeros[depth][1]

        # 가로, 세로, 3x3에 내가 대체하려는 숫자가 존재하는지 확인
        if garo(nr, i) and sero(nc, i) and bythree(nr, nc, i):
            sudoku[nr][nc] = i
            dfs(depth + 1)
            sudoku[nr][nc] = 0

sudoku = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]
dfs(0)