# BFS + 상태관리
# 벽 부수고 이동하기 문제와 유사.
# visited 배열을 3중배열로 만들어서 말처럼 이동한 경우/ 원숭이로 이동한 경우를 구별
# r, c 좌표로 말처럼 k번 이동했으면 visited[r][c][k]에 이동거리 저장
# r, c 좌표로 원숭이로 이동했으면 k는 변하지 않는다
# 그리고 (H, W)까지 갔다면 저장했던 거리를 리턴, 아니라면 -1을 리턴해 출력

import sys
input = sys.stdin.readline
from collections import deque

# 말 8방향
hr = (-2, -1, 1, 2, 2, 1, -1, -2)
hc = (1, 2, 2, 1, -1, -2, -2, -1)

# 원숭이 4방향
mr = (-1, 1, 0, 0)
mc = (0, 0, -1, 1)

def bfs():
    visited = [[[0] * W for _ in range(H)] for _ in range(K+1)]
    Q = deque([(0, 0, 0)])
    while Q:
        r, c, cnt = Q.popleft()
        if r == H-1 and c == W-1:
            return visited[cnt][r][c]
        if cnt < K:     # 기회 남아있으면 말 걸음
            for d in range(8):
                nr = r + hr[d]
                nc = c + hc[d]
                if not (0 <= nr < H and 0 <= nc < W) or A[nr][nc]:
                    continue
                if not visited[cnt+1][nr][nc]:
                    visited[cnt+1][nr][nc] = visited[cnt][r][c] + 1
                    Q.append((nr, nc, cnt+1))
        # 원숭이 걸음
        for d in range(4):
            nr = r + mr[d]
            nc = c + mc[d]
            if not (0 <= nr < H and 0 <= nc < W) or A[nr][nc]:
                continue
            if not visited[cnt][nr][nc]:
                visited[cnt][nr][nc] = visited[cnt][r][c] + 1
                Q.append((nr, nc, cnt))
    return -1

# main
K = int(input())
W, H = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
print(bfs())