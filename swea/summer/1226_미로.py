import sys
sys.stdin = open("1226_input.txt")

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# Queue로 풀기
# def bfs(sr, sc):
#     global maze, flag, visited
#     Q = [(sr, sc)]
#     visited[sr][sc] = 1
#
#     while Q:
#         r, c = Q.pop(0)
#         if maze[r][c] == 3:
#             flag = 1
#             return
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if not (0 <= nr < 16) and (0 <= nc < 16):
#                 continue
#             if maze[nr][nc] == 1:
#                 continue
#             if visited[nr][nc] == 0:
#                 Q.append((nr, nc))
#                 visited[nr][nc] = 1

# Stack으로 풀기
# def dfs(sr, sc):
#     global maze, flag
#     S = [(sr, sc)]
#     while S:
#         r, c = S.pop()
#         if maze[r][c] == 3:
#             flag = 1
#             return
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if not (0 <= nr < 16) and (0 <= nc < 16):
#                 continue
#             if maze[nr][nc] == 1:
#                 continue
#             if visited[nr][nc] == 1:
#                 continue
#             S.append((nr, nc))
#             visited[nr][nc] = 1

# 재귀로 풀기
def dfs(sr, sc):
    global maze, flag

    for i in range(4):
        nr = sr + dr[i]
        nc = sc + dc[i]
        if maze[nr][nc] == 1:
            continue
        if maze[nr][nc] == 3:
            flag = 1
            return
        maze[nr][nc] = 1
        dfs(nr, nc)

for tc in range(10):
    T = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    flag = 0
    # bfs(1, 1)
    dfs(1, 1)
    print("#{} {}".format(tc+1, flag))