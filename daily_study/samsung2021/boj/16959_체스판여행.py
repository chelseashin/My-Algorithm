# 참고 : https://github.com/gogumasitda/TIL/blob/master/algorithm/0321

import sys
input = sys.stdin.readline
import queue

# 나이트 : 해당 8방향
knight_dr = (-1, -1, -2, -2, 2, 2, 1, 1)
knight_dc = (-2, 2, -1, 1, -1, 1, -2, 2)

# 룩 : 대각선 이동
rook_dr = (0, 0, 1, -1)
rook_dc = (1, -1, 0, 0)

# 비숍 : 직선 이동
bishop_dr = (1, -1, 1, -1)
bishop_dc = (1, -1, -1, 1)

def bfs(r, c, p, s, t):
    global goal
    visited[r][c][s][p] = 1
    q.put([r, c, p, s, t])
    while not q.empty():
        row, col, piece, start, time = q.get()
        if raw[row][col] == start + 1:
            start += 1
            if start == goal:
                return time

        nexttime = time + 1
        for i in range(1, 3):               # 말 바꾸기
            nextpiece = (piece + i) % 3
            if visited[row][col][start][nextpiece] == -1:
                visited[row][col][start][nextpiece] = 1
                q.put([row, col, nextpiece, start, nexttime])

        # knight
        if piece == 0:
            for i in range(8):
                nr = row + knight_dr[i]
                nc = col + knight_dc[i]
                if N > nr >= 0 and N > nc >= 0 and visited[nr][nc][start][piece] == -1:
                    visited[nr][nc][start][piece] = 1
                    q.put([nr, nc, piece, start, time + 1])

        # rook
        elif piece == 1:
            for i in range(4):
                for dis in range(1, N+1):
                    nr = row + rook_dr[i] * dis
                    nc = col + rook_dc[i] * dis
                    if N > nr >= 0 and N > nc >= 0:
                        if visited[nr][nc][start][piece] == -1:
                            visited[nr][nc][start][piece] = 1
                            q.put([nr, nc, piece, start, time + 1])
                    else:
                        break
        # bishop
        else:
            for i in range(4):
                for dis in range(1, N+1):
                    nr = row + bishop_dr[i] * dis
                    nc = col + bishop_dc[i] * dis
                    if N > nr >= 0 and N > nc >= 0:
                        if visited[nr][nc][start][piece] == -1:
                            visited[nr][nc][start][piece] = 1
                            q.put([nr, nc, piece, start, time + 1])
                    else:
                        break
    return float('inf')

# main
N = int(input())
D = dict()
raw = []
start, goal = 1, N*N
sr, sc = 0, 0
for i in range(N):
    raw.append(list(map(int, input().split())))
    for j in range(N):
        if raw[i][j] == start:
            sr, sc = i, j

time = 0
min_time = float('inf')
for p in range(3):  # 나이트, 룩, 비숍 중 하나를 1이 있는 칸에 놓으며 시작
    q = queue.Queue()
    visited = [[[[-1] * 3 for _ in range(N*N+1)] for _ in range(N)] for _ in range(N)]
    each = bfs(sr, sc, p, start, time)
    min_time = min(min_time, each)
print(min_time)