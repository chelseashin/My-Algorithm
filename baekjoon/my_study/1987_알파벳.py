import sys
sys.stdin = open('1987_input.txt')
input = sys.stdin.readline
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dfs(r, c, cnt):
    global MAX
    MAX = max(MAX, cnt)
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if not (0 <= nr < R and 0 <= nc < C):
            continue
        temp = ord(A[nr][nc])
        if visited[temp - 65]:
            continue
        visited[temp - 65] = 1
        dfs(nr, nc, cnt+1)
        visited[temp - 65] = 0

# main
R, C = map(int, input().split())
A = [list(input()) for _ in range(R)]
MAX = float('-inf')
visited = [0] * 26
visited[ord(A[0][0]) - 65] = 1
dfs(0, 0, 1)
print(MAX)