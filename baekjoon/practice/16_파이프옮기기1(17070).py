import sys
sys.stdin = open('16_input.txt')

def dfs(r, c, dir):
    global arr, count
    if r == N-1 and c == N-1:
        count += 1
        return

    # 가로방향
    if dir == 1:
        if c+1 < N and arr[r][c+1] == 0:
            dfs(r, c+1, 1)
        if r+1 < N and c+1 < N and arr[r+1][c] == 0 and arr[r][c+1] == 0 and arr[r+1][c+1] == 0:
            dfs(r+1, c+1, 3)
    # 세로방향
    elif dir == 2:
        if r+1 < N and arr[r+1][c] == 0:
            dfs(r+1, c, 2)
        if r+1 < N and c+1 < N and arr[r+1][c] == 0 and arr[r][c+1] == 0 and arr[r+1][c+1] == 0:
            dfs(r+1, c+1, 3)
    # 대각선방향
    elif dir == 3:
        if c+1 < N and arr[r][c+1] == 0:
            dfs(r, c+1, 1)
        if r+1 < N and arr[r+1][c] == 0:
            dfs(r+1, c, 2)
        if r+1 < N and c+1 < N and arr[r+1][c] == 0 and arr[r][c+1] == 0 and arr[r+1][c+1] == 0:
            dfs(r+1, c+1, 3)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

count = 0
dfs(0, 1, 1)
print(count)