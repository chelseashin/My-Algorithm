import sys
sys.stdin = open('14_input.txt')

# 상, 우, 하, 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(sr, sc, sd):
    global N, M, arr, count
    Q = [(sr, sc, sd)]
    arr[sr][sc] = 10
    count += 1
    while Q:
        r, c, d = Q.pop(0)
        for i in range(4):
            d = (d - 1) % 4
            nr = r + dr[d]
            nc = c + dc[d]
            if not (1 <= nr < N-1 and 1 <= nc < M-1):
                continue
            if arr[nr][nc] == 1:
                continue
            if arr[nr][nc] == 0:
                arr[nr][nc] = arr[r][c] + 1
                count += 1
                Q.append((nr, nc, d))
                break
        else:
            # 후진할 수 있을 때
            nr = r - dr[d]
            nc = c - dc[d]
            # 후진 못할 때
            if not (1 <= nr < N-1 and 1 <= nc < M-1):
                break
            if arr[nr][nc] == 1:
                break
            Q.append((nr, nc, d))
            arr[nr][nc] = arr[r][c]
    # print(arr[r][c] - 9)


N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
count = 0

bfs(r, c, d)
print(count)