# 모든 행과 모든 열에 한 명 이상의 경비원이 있어야 함.
# 행 열 기준으로 필요한 경비원의 수를 각각 계산하여 더 큰 수를 출력.

N, M = map(int, input().split())

row = [0] * N
col = [0] * M
A = []

for i in range(N):
    A.append(input())
    for j in range(M):
        if A[i][j] == "X":      # 경비원 표시
            row[i] = 1
            col[j] = 1

row_cnt, col_cnt = 0, 0
for i in range(N):
    if row[i] == 0:
        row_cnt += 1
for j in range(M):
    if col[j] == 0:
        col_cnt += 1
print(max(row_cnt, col_cnt))