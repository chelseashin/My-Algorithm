import sys
sys.stdin = open("16509_input.txt")

# 상이 갈 수 있는 곳
dr = (-2, 2, 3, 3, 2, -2, -3, -3)
dc = (3, 3, 2, -2, -3, -3, -2, 2)

# 장애물 검사
wall = ([(0,1),(-1,2)],[(0,1),(1,2)],
        [(1,0),(2,1)],[(1,0),(2,-1)],
        [(0,-1),(1,-2)],[(0,-1),(-1,-2)],
        [(-1,0),(-2,-1)],[(-1,0),(-2,1)])

def bfs(sr, sc):
    global arr, rk, ck
    visited = [[0] * 9 for _ in range(10)]
    Q = [(sr, sc)]
    visited[sr][sc] = 1
    while Q:
        r, c = Q.pop(0)
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < 10 and 0 <= nc < 9):
                continue
            if visited[nr][nc]:
                continue
            flag = 0
            for j in wall[i]:
                if rk == r+j[0] and ck == c+j[1]:
                    flag = 1
            if flag:
                continue
            Q.append((nr, nc))
            visited[nr][nc] = visited[r][c] + 1
            if nr == rk and nc == ck:
                return visited[nr][nc] - 1
    return -1

arr = [[0] * 9 for _ in range(10)]
rs, cs = map(int, input().split())   # 상 위치
rk, ck = map(int, input().split())   # 왕 위치

print(bfs(rs, cs))