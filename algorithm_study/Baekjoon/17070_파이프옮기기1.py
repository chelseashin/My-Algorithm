import sys
sys.stdin = open('17070_input.txt')

# 시작좌표, 방향
def dfs(r, c, d):
    global N, A, ans
    # 도착 조건
    if r == N-1 and c == N-1:
        ans += 1
        return

    # 가로
    if d == 1:
        if c+1 < N and A[r][c+1] == 0:
            dfs(r, c+1, 1)
        if r+1 < N and c+1 < N and A[r][c+1] == 0 and A[r+1][c] == 0 and A[r+1][c+1] == 0:
            dfs(r+1, c+1, 3)

    # 세로
    elif d == 2:
        if r+1 < N and A[r+1][c] == 0:
            dfs(r+1, c, 2)
        if r+1 < N and c+1 < N and A[r][c+1] == 0 and A[r+1][c] == 0 and A[r+1][c+1] == 0:
            dfs(r+1, c+1, 3)

    # 대각선
    else:
        if c+1 < N and A[r][c+1] == 0:
            dfs(r, c+1, 1)
        if r+1 < N and A[r+1][c] == 0:
            dfs(r+1, c, 2)
        if r+1 < N and c+1 < N and A[r][c+1] == 0 and A[r+1][c] == 0 and A[r+1][c+1] == 0:
            dfs(r+1, c+1, 3)


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

ans = 0
dfs(0, 1, 1)
print(ans)