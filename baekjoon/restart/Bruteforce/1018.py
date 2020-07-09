import sys
sys.stdin = open('1018_input.txt')

# 실패코드
# dr = (-1, 1, 0, 0)
# dc = (0, 0, -1, 1)
#
# def solution(sr, sc):
#     global chess, cnt, N, M, MIN, visited
#     cnt = 0
#
#     Q = [(sr, sc)]
#     visited[sr][sc] = 1
#
#     while Q:
#         r, c = Q.pop(0)
#         temp = chess[r][c]
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if not (sr <= nr < sr+8 and sc <= nc < sc+8):
#                 continue
#             if visited[nr][nc]:
#                 continue
#             if chess[nr][nc] == temp and visited[nr][nc] == 0:
#                 cnt += 1
#                 if chess[nr][nc] == "B":
#                     chess[nr][nc] = "W"
#                 else:
#                     chess[nr][nc] = "B"
#                 visited[nr][nc] = 1
#             if visited[nr][nc] == 0:
#                 Q.append((nr, nc))
#                 visited[nr][nc] = 1

# 성공코드
def solution(r, c):
    global MIN, cnt
    check_color = ['B', 'W']
    for color in range(2):
        cnt = 0
        for nr in range(r, r+8):
            for nc  in range(c, c+8):
                if chess[nr][nc] != check_color[color%2]:
                    cnt += 1
                color += 1
            color += 1
        if MIN > cnt:
            MIN = cnt

N, M = map(int, input().split())
chess = [list(input()) for _ in range(N)]
MIN = float('inf')

for i in range(N-7):
    for j in range(M-7):
        solution(i, j)

print(MIN)