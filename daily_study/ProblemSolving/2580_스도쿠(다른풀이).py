import sys
input = sys.stdin.readline

def solve(depth):
    if depth == N:
        for array in A:
            print(*array)
        exit()
    r = B[depth] // 9
    c = B[depth] % 9
    for num in range(1, 10):
        temp = r//3*3 + c//3
        if not (row[r][num] or col[c][num] or squ[temp][num]):
            row[r][num], col[c][num], squ[temp][num] = 1, 1, 1
            A[r][c] = num
            solve(depth+1)
            A[r][c] = 0
            row[r][num], col[c][num], squ[temp][num] = 0, 0, 0

A = [list(map(int, input().split())) for _ in range(9)]
B = [0] * 81
row = [[0] * 10 for _ in range(9)]      # 가로 정보
col = [[0] * 10 for _ in range(9)]      # 세로 정보
squ = [[0] * 10 for _ in range(9)]      # 3*3 정보

N = 0
for i in range(9):
    for j in range(9):
        n = A[i][j]
        if n:
            row[i][n] = 1
            col[j][n] = 1
            squ[i//3*3 + j//3][n] = 1
        else:
            B[N] = i * 9 + j  # 0일 때, 몇 번째 칸이 비어있는지
            N += 1
solve(0)