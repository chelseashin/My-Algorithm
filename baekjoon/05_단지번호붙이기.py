import sys
sys.stdin = open("05_input.txt")

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(sr, sc):
    global arr, N, cnt
    Q = [(sr, sc)]
    while Q:
        r, c = Q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if arr[nr][nc] == 0:
                continue
            if arr[nr][nc] == 1:
                cnt += 1
                arr[nr][nc] = 0
                Q.append((nr, nc))

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
# print(arr)

count = 0
L = []
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            cnt = 0
            bfs(i, j)
            count += 1
            L.append(cnt)

print(count)
for i in sorted(L):
    print(i)