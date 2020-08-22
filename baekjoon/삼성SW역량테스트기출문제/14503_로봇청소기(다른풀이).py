import sys
sys.stdin = open('14503_input.txt')

# 로봇청소기의 움직임을 bfs로 구현
# 이동 경로를 거리로 표시하면서 움직임
# 2부터 시작하기 때문에 마지막 거리에서 -1 해줌
# 방향 잘 넘겨주 기

from collections import deque

# 북동남서
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

def bfs(sr, sc, sd):
    Q = deque([(sr, sc, sd)])
    arr[sr][sc] = 2
    while Q:
        r, c, d = Q.popleft()
        for i in range(4):
            d = (d-1) % 4
            nr = r + dr[d]
            nc = c + dc[d]
            if not (1 <= nr < N-1 and 1 <= nc < M-1):
                continue
            if arr[nr][nc] == 1:
                continue
            if arr[nr][nc] == 0:    # 공간 비어있을 때만 청소
                arr[nr][nc] = arr[r][c] + 1
                Q.append((nr, nc, d))
                break
        # 4방향 모두 벽이거나 이미 청소했다면
        else:
            nr = r - dr[d]
            nc = c - dc[d]
            if not (1 <= nr < N-1 and 1 <= nc < M-1):
                break
            if arr[nr][nc] == 1:
                break
            # 후진
            Q.append((nr, nc, d))
            arr[nr][nc] = arr[r][c]
    # print(arr)
    return arr[r][c] - 1

# 다른 풀이
N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

print(bfs(r, c, d))