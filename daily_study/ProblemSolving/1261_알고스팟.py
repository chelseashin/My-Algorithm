from sys import stdin
input = stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs():
    check = [[float('inf') for _ in range(C)] for _ in range(R)]
    check[0][0] = 0
    
    Q = deque([(0, 0)])
    while Q:
        r, c = Q.popleft()
        if (r, c) == (R-1, C-1):        # 목적지 도착
            return check[R-1][C-1]
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            # 빈 공간일 때 벽 부순 횟수가 적게 걸린 값일 때만 갱신
            if A[nr][nc] == '0':
                if check[nr][nc] > check[r][c]:
                    check[nr][nc] = check[r][c]
                    Q.appendleft((nr, nc))      # 빈 공간이면 큐의 앞쪽으로 넣어줌
            
            # 벽 만났을 때 벽 부순 횟수가 적게 걸린 값일 때만 갱신
            else:
                if check[nr][nc] > check[r][c] + 1:
                    check[nr][nc] = check[r][c] + 1
                    Q.append((nr, nc))

# main
C, R = map(int, input().split())
A = [list(input().strip()) for _ in range(R)]
print(bfs())