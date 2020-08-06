import sys
sys.stdin = open('17070_input.txt')

# 가로, 세로, 대각선 방향
dir = [[(0, 1), (1, 1)], [(1, 0), (1, 1)], [(0, 1), (1, 1), (1, 0)]]

def searchD(dr, dc):
    if dr == 0 and dc == 1:
        return 0
    if dr == 1 and dc == 0:
        return 1
    if dr == 1 and dc == 1:
        return 2

# 방법 2 - Memoization
def dfs(r, c, d):
    global cnt
    # print(memo)
    if r == N-1 and c == N-1:
        return 1
    if memo[r][c][d] != -1:
        return memo[r][c][d]
    memo[r][c][d] = 0
    for dr, dc in dir[d]:
        nr, nc, nd = r+dr, c+dc, searchD(dr, dc)
        if not (0 <= nr < N and 0 <= nc < N):
            continue
        if A[nr][nc]:
            continue
        if nd == 2 and (A[nr][nc-1] or A[nr-1][nc]):
            continue
        memo[r][c][d] += dfs(nr, nc, nd)
    return memo[r][c][d]

# # 시간초과
# def dfs(r, c, d):
#     global cnt
#     if r == N-1 and c == N-1:
#         cnt += 1
#         return
#     for dr, dc in dir[d]:
#         nr, nc, nd = r+dr, c+dc, searchD(dr, dc)
#         if not (0 <= nr < N and 0 <= nc < N):
#             continue
#         if A[nr][nc]:
#             continue
#         if nd == 2 and (A[nr][nc-1] or A[nr-1][nc]):
#             continue
#         dfs(nr, nc, nd)
#     return

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

# 방법 1
memo = [[[-1] * 3 for _ in range(N)] for _ in range(N)]
print(dfs(0, 1, 0))
# print(memo)

# 방법 2
# cnt = 0
# dfs(0, 1, 0)
# print(cnt)