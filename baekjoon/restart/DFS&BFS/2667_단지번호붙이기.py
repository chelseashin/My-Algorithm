import sys
sys.stdin = open('2667_input.txt')

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs(sr, sc):
    global cnt, temp
    Q = [(sr, sc)]
    arr[sr][sc] = 0
    while Q:
        r, c = Q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if not arr[nr][nc]:
                continue
            arr[nr][nc] = 0
            temp += 1
            Q.append((nr, nc))

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
total = []
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            temp = 1
            bfs(i, j)
            total.append(temp)

print(len(total))
for t in sorted(total):
    print(t)