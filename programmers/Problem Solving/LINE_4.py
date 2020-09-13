maze = [[0, 1, 0, 1],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 1, 0]]

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(sr, sc, cnt, N, maze):
    if sr == N-1 and sc == N-1:
        return cnt
    if maze[sr][sc+1] or (0 <= sr < N and 0 <= sc+1 < N):      # 방향은 아래
        dir = 1
        nr = sr + dr[dir]
        nc = sc + dc[dir]
        if not maze[nr][nc] and (0 <= nr < N and 0 <= nc < N):
            dfs(nr, nc, cnt+1, N, maze)
    elif maze[sr+1][sc] and (0 <= sr < N and 0 <= sc + 1 < N):  # 방향 오른쪽
        dir = 3
        nr = sr + dr[dir]
        nc = sc + dc[dir]
        if not maze[nr][nc] and (0 <= nr < N and 0 <= nc < N):
            dfs(nr, nc, cnt+1, N, maze)
    return cnt

def solution(maze):
    N = len(maze)
    answer = dfs(0, 0, 0, N, maze)
    return answer

print(solution(maze))