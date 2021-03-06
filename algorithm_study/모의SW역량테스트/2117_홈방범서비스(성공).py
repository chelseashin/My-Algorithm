import sys
sys.stdin = open("2117_input.txt")

from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs(sr, sc):
    global N, M, MAX, K
    visited = [[0] * N for _ in range(N)]
    Q = deque([(sr, sc)])
    visited[sr][sc] = 1
    cnt = 0
    for depth in range(1, 25):
        time = len(Q)
        for i in range(time):
            r, c = Q.popleft()
            if city[r][c]:
                cnt += 1
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                if visited[nr][nc]:
                    continue
                visited[nr][nc] = 1
                Q.append((nr, nc))
        # 보안회사의 이익이 0보다 크면
        if M * cnt - K[depth] >= 0:
            MAX = max(MAX, cnt)
    return

# K에 따른 운영비용 리스트
K = [0] + [k * k + (k-1) * (k-1) for k in range(1, 25)]

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    MAX = 0
    for i in range(N):
        for j in range(N):
            # 중심 정하기
            bfs(i, j)
    print("#{} {}".format(tc+1, MAX))

#1 5
#2 4
#3 24
#4 48
#5 3
#6 65
#7 22
#8 22
#9 78
#10 400