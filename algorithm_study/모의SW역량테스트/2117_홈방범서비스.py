import sys
sys.stdin = open("2117_input.txt")

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def check():
    global city, visited, MAX, M
    cnt = 0  # 서비스 영역
    pay = 0  # 운영 비용
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                cnt += 1
                if city[i][j]:
                    pay += 1

    # 보안회사의 이익
    temp = pay * M - cnt
    if temp > MAX:
        MAX = temp
    return MAX

# 길이 K에 따라 마름모 visited 구하기(BFS)
def bfs(sr, sc, L):
    global N, visited, Q
    dis = visited[sr][sc]
    while Q:
        r, c = Q.pop(0)
        if dis == L+1:
            break
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if visited[nr][nc]:
                continue
            visited[nr][nc] = visited[r][c] + 1
            Q.append((nr, nc))
            dis = visited[r][c] + 1
    print(visited)
    check()

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]

    # 운영영역 K 구하기
    MAX = float('-inf')
    for i in range(N):
        for j in range(N):
            visited = [[0] * N for _ in range(N)]
            Q = [(i, j)]
            visited[i][j] = 1
            for k in range(1, N):
                bfs(i, j, k)
    print("#{} {}".format(tc+1, MAX))