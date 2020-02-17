import sys
sys.stdin = open("1249_input.txt")

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs(sr, sc):
    global A, N, Q
    D[sr][sc] = 0
    while Q:
        r, c = Q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            time = A[nr][nc]
            if D[nr][nc] > D[r][c] + time:
                D[nr][nc] = D[r][c] + time
                Q.append((nr, nc))

T = int(input())
for tc in range(T):
    N = int(input())
    A = [list(map(int, input())) for _ in range(N)]
    D = [[float('inf')] * N for _ in range(N)]
    Q = [(0, 0)]
    bfs(0, 0)
    print("#{} {}".format(tc+1, D[N-1][N-1]))

#1 2
#2 2
#3 8
#4 57
#5 151
#6 257
#7 18
#8 160
#9 414
#10 395