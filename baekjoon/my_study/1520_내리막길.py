import sys
sys.stdin = open('1520_input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dfs(r, c):
    if r == 0 and c == 0:
        return 1
    if visited[r][c] == -1:
        visited[r][c] = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if A[r][c] < A[nr][nc]:
                visited[r][c] += dfs(nr, nc)
    return visited[r][c]

# main
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

visited = [[-1] * M for _ in range(N)]
print(dfs(N-1, M-1))
# for v in visited:
#     print(v)
# print(visited[N-1][M-1])



# 시간초과
# def dfs(r, c):
#     global result, N, M
#     if r == N-1 and c == M-1:
#         # for v in visited:
#         #     print(v)
#         # print()
#         result += 1
#         return
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if not (0 <= nr < N and 0 <= nc < M):
#             continue
#         if visited[nr][nc]:
#             continue
#         if A[r][c] > A[nr][nc]:
#             visited[nr][nc] = 1
#             dfs(nr, nc)
#             visited[nr][nc] = 0

# dfs + dp로 목적지까지 도착할 수 있는지 검사한다
# 루프를 방지하기 위해 방문 확인 배열 c를 -1로 초기화하고 이동할 때마다 0으로 다시 설정해준다
# 1. 과정을 진행하면서 c에 이미 저장된 값이 0이면 목적지까지 갈 수 없으므로 0을 반환한다
# 2. 1 이상의 값이면 이전에 그만큼 방문 경로가 있으므로 해당 값을 반환해서 더해준다
# 3. -1이면 방문하지 않은 경로이므로 dfs + dp 수행
