import sys
sys.stdin = open('17070_input.txt')
input = sys.stdin.readline

def dfs(r, c, dir):
    global result
    if r == N-1 and c == N-1:
        result += 1
        return
    # 가로
    if dir == 0:
        if (0 <= r < N and 0 <= c+1 < N) and not A[r][c+1]:
            dfs(r, c+1, 0)
        if (0 <= r+1 < N and 0 <= c+1 < N) and not A[r][c+1] and not A[r+1][c] and not A[r+1][c+1]:
            dfs(r+1, c+1, 2)
    # 세로
    elif dir == 1:
        if (0 <= r+1 < N and 0 <= c < N) and not A[r+1][c]:
            dfs(r+1, c, 1)
        if (0 <= r+1 < N and 0 <= c+1 < N) and not A[r][c+1] and not A[r+1][c] and not A[r+1][c+1]:
            dfs(r+1, c+1, 2)
    # 대각선
    else:
        if (0 <= r < N and 0 <= c+1 < N) and not A[r][c+1]:
            dfs(r, c+1, 0)
        if (0 <= r+1 < N and 0 <= c < N) and not A[r+1][c]:
            dfs(r+1, c, 1)
        if (0 <= r+1 < N and 0 <= c+1 < N) and not A[r][c+1] and not A[r+1][c] and not A[r+1][c+1]:
            dfs(r+1, c+1, 2)

# main
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
result = 0
dfs(0, 1, 0)
print(result)
