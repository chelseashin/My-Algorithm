import sys
sys.stdin = open("1949_input.txt")

# swea 모의 테스트 문제

# 문제 정리
# 1. 등산로는 가장 높은 봉우리에서 시작
# 2. 등산로는 높은 지형에서 낮은 지형으로 가로 또는 세로 연결
# 2. 1. 높이가 같은 곳 대각선 연결 불가
# 3. 긴 등사로를 만들기 위해 딱 한 곳을 정해 최대 K 만큼 지형 깎기 가능.
# 4. 가장 긴 등산로 길이 출력

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dfs(sr, sc, flag):
    global N, K, max_length
    if max_length < visited[sr][sc]:
        max_length = visited[sr][sc]
    for i in range(4):
        nr = sr + dr[i]
        nc = sc + dc[i]
        if not (0 <= nr < N and 0 <= nc < N):
            continue
        if visited[nr][nc]:
            continue
        if A[nr][nc] < A[sr][sc]:
            visited[nr][nc] = visited[sr][sc] + 1
            dfs(nr, nc, flag)
            visited[nr][nc] = 0
        else:
            if flag or A[nr][nc] - K >= A[sr][sc]:
                continue
            flag = 1
            temp = A[nr][nc]
            A[nr][nc] = A[sr][sc] - 1
            visited[nr][nc] = visited[sr][sc] + 1
            dfs(nr, nc, flag)
            visited[nr][nc] = 0
            A[nr][nc] = temp
            flag = 0

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    max_height = 0
    max_length = 0

    for i in range(N):
        for j in range(N):
            if A[i][j] > max_height:
                max_height = A[i][j]

    for i in range(N):
        for j in range(N):
            if A[i][j] == max_height:
                flag = 0
                visited[i][j] = 1
                dfs(i, j, flag)
                visited[i][j] = 0

    print("#{} {}".format(tc+1, max_length))