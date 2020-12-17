import sys
sys.stdin = open('1520_input.txt')
input = sys.stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dfs(r, c):
    global result, N, M
    if r == N-1 and c == M-1:
        # for v in visited:
        #     print(v)
        # print()
        result += 1
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if not (0 <= nr < N and 0 <= nc < M):
            continue
        if visited[nr][nc]:
            continue
        if A[r][c] > A[nr][nc]:
            visited[nr][nc] = 1
            dfs(nr, nc)
            visited[nr][nc] = 0

# main
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
result = 0
dfs(0, 0)
print(result)