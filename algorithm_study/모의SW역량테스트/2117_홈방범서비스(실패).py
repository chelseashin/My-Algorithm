import sys
sys.stdin = open("2117_input.txt")

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def check(K):
    global city, visited, MAX, M
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] and city[i][j]:
                cnt += 1

    # 보안회사의 이익이 0보다 크면
    temp = cnt * M - (K*K + (K-1)*(K-1))
    if temp > 0:
        MAX = max(cnt, MAX)
        print(cnt)
    return MAX

# 길이 K에 따라 마름모 visited 구하기(BFS)
def bfs(sr, sc, K):
    global N, visited, Q
    visited = [[0] * N for _ in range(N)]
    if K == 1:
        visited[sr][sc] = 1
        # check(K)
        print(visited)
        return
    Q = [(sr, sc)]
    visited[sr][sc] = 1
    dis = visited[sr][sc]
    while Q:
        r, c = Q.pop(0)
        if dis == K:
            return
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if visited[nr][nc]:
                continue
            visited[nr][nc] = 1
            Q.append((nr, nc))
        dis = visited[r][c] + 1
    print(visited)
    return

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]

    MAX = 0
    for i in range(N):
        for j in range(N):
            # 중심 정하면 운영영역 k 구하기
            for k in range(1, N):
                visited = [[0] * N for _ in range(N)]
                bfs(i, j, k)
                check(k)
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