import sys
sys.stdin = open("2105_input.txt")

# 우하, 좌하, 좌상, 우상
dr = (1, 1, -1, -1)
dc = (1, -1, -1, 1)

def DFS(d, r, c):
    global sr, sc, cafe, visited, N, result
    for i in range(2):
        if (d + i) == 4:
            return
        nr = r + dr[d + i]
        nc = c + dc[d + i]
        if not (0 <= nr < N and 0 <= nc < N):
            continue
        if nr == sr and nc == sc:
            result = max(result, sum(visited))
            return
        if visited[cafe[nr][nc]]:
            continue
        visited[cafe[nr][nc]] = 1
        DFS(d + i, nr, nc)
        visited[cafe[nr][nc]] = 0


T = int(input())
for tc in range(T):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * 101
    result = -1
    for i in range(N-2):
        for j in range(1, N-1):
            visited[cafe[i][j]] = 1
            sr, sc = i, j
            DFS(0, sr, sc)
            visited[cafe[i][j]] = 0
    print("#{} {}".format(tc+1, result))

#1 6
#2 -1
#3 4
#4 4
#5 8
#6 6
#7 14
#8 12
#9 18
#10 30