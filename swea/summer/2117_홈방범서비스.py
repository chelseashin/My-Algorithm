import sys
sys.stdin = open("2117_input.txt")

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dfs(sr, sc):
    global N, M, MAX, K
    visited = [[0] * N for _ in range(N+1)]
    Q = [(sr, sc)]
    visited[sr][sc] = 1
    cnt = 0
    for K in range(1, 50):
        time = len(Q)
        for i in range(time):
            r, c = Q.pop(0)
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
        # 보안회사의 이익이 0보다 크거나 같으면
        if M * cnt >= K**2+(K-1)**2:
            MAX = max(MAX, cnt)
    return

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    MAX = 0
    # 중심 정하기
    for i in range(N):
        for j in range(N):
            dfs(i, j)
    # print(city)
    print("#{} {}".format(tc+1, MAX))