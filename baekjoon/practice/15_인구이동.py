import sys
sys.stdin = open('15_input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(sr, sc, Q):
    global N, L, R, visited, result
    total, count = 0, 0
    temp = []
    while Q:
        r, c = Q.pop(0)
        total += ingu[r][c]
        count += 1
        temp.append((r, c))
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nc < N and 0 <= nc < N):
                continue
            if visited[nr][nc]:
                continue
            if not (L <= abs(ingu[r][c] - ingu[nr][nc]) <= R):
                continue
            Q.append((nr, nc))
            visited[nr][nc] = 1
    if count == 1:
        return 0
    avg = total // count
    for r, c in temp:
        ingu[r][c] = avg
    return 1

def start():
    global N, result
    flag = 1
    while flag:
        flag = 0

        for i in range(N):
            for j in range(N):

                if visited[i][j]:
                    continue
                Q = [(i, j)]
                visited[i][j] = 1
                if bfs(i, j, Q):
                    flag = 1
        if flag:
            result += 1

N, L, R = map(int, input().split())
ingu = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
result = 0
start()
print(result)