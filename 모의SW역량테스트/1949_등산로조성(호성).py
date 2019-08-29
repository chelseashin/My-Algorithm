import sys
sys.stdin = open('1949_input.txt')

def DFS(x, y, distance, visited, chance):
    global max_distance
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if visited[nx][ny] != 0:
            continue
        if data[x][y]+K > data[nx][ny] >= data[x][y] and visited[nx][ny] == 0 and chance == 1:
            chance = 0
            for i in range(1, K+1):
                data[nx][ny] -= i
                if data[nx][ny] < data[x][y] and visited[nx][ny] == 0:
                    visited[nx][ny] = 99
                    if max_distance <= distance+1:
                        max_distance = distance+1
                    DFS(nx, ny, distance+1, visited, chance)
                    visited[nx][ny] = 0
                data[nx][ny] += i
            chance = 1
        if data[nx][ny] < data[x][y] and visited[nx][ny] == 0:
            visited[nx][ny] = 99
            if max_distance <= distance+1:
                max_distance = distance+1
            DFS(nx, ny, distance+1, visited, chance)
            visited[nx][ny] = 0


T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]

    top_check = []
    top = 0
    for i in range(N):
        for j in range(N):
            if top <= data[i][j]:
                top = data[i][j]

    max_distance = -987654321
    for i in range(N):
        for j in range(N):
            if data[i][j] == top:
                visited[i][j] = 99
                DFS(i, j, 1, visited, 1)
                visited[i][j] = 0

    print('#{} {}'.format(test_case, max_distance))