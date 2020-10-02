import sys
sys.stdin = open('1949_input.txt')

# 상하좌우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dfs(r, c, chance):
    global visited, result
    result = max(result, visited[r][c])
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if not (0 <= nr < N and 0 <= nc < N):
            continue
        if visited[nr][nc]:
            continue
        if A[nr][nc] < A[r][c]:
            visited[nr][nc] = visited[r][c] + 1
            dfs(nr, nc, chance)
            visited[nr][nc] = 0
        else:
            if not chance:
                continue
            # 기회 가지고 있고, 깎은 상태가 현 위치보다 낮아야만 함.
            if A[nr][nc] - K < A[r][c]:
                temp = A[nr][nc]
                A[nr][nc] = A[r][c] - 1
                visited[nr][nc] = visited[r][c] + 1
                dfs(nr, nc, chance-1)
                visited[nr][nc] = 0
                A[nr][nc] = temp

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    result = float('-inf')

    top = 0     # 최대 높이 찾기
    for i in range(N):
        for j in range(N):
            if A[i][j] > top:
                top = A[i][j]

    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[i][j] == top:
                visited[i][j] = 1   # 방문
                dfs(i, j, 1)
                visited[i][j] = 0

    print('#{} {}'.format(tc+1, result))