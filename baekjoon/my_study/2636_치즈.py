import sys
sys.stdin = open("2636_input.txt")
from collections import deque
input = sys.stdin.readline
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def melting(sr, sc):
    Q = deque([(sr, sc)])
    visited = [[-1] * M for _ in range(N)]      # -1, 0, 1으로 상태 구분
    visited[sr][sc] = 0
    meltCnt = 0
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if visited[nr][nc] >= 0:
                continue
            if visited[nr][nc] == -1 and A[nr][nc]:     # 방문 X, 치즈와 맞닿는 부분 녹이기
                visited[r][c] = 0
                visited[nr][nc] = 1     # 녹일 부분 1로 표시
                meltCnt += 1
                continue
            visited[nr][nc] = 0
            Q.append((nr, nc))

    for i in range(N):
        for j in range(M):
            if visited[i][j] > 0:
                A[i][j] = 0             # 치즈 녹이기
    return meltCnt

# main
N, M = map(int, input().split())
A = []
cheeze = 0
for i in range(N):
    A.append(list(map(int, input().split())))
    for j in range(M):
        if A[i][j]:
            cheeze += 1
time = 0
while True:
    time += 1
    temp = melting(0, 0)    # 녹인 갯수 리턴
    cheeze -= temp
    if not cheeze:
        print(time)
        print(temp)
        break