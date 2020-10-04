import sys
sys.stdin = open('19237_input.txt')
from collections import deque

# Simulation

def bfs():
    global A, Q
    time = 0
    while Q:
        if time > 1000:
            return -1
        r, c, info = Q.popleft()    # 상어의 좌표와 정보
        n, d, s = info  # 상어 번호, 방향, 남은 냄새
        # print(r, c, n, d, s)
        for i in range(4):
            # 상어별 우선순위에 따른 새로운 방향
            nd = shark_dir[n][d][i] - 1
            print(nd)
            # print(shark_dir[n-1])
            # print(n,'번 상어', d,"=>", nd)
            nr = r + dr[nd]
            nc = c + dc[nd]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            # 칸 비어있거나 이동할 방향에 있는 상어 번호가 내 번호보다 작은 경우
            if not A[nr][nc] or A[nr][nc][0] > A[r][c][0]:
                A[nr][nc] = [n, nd, K]  # 새 칸으로 이동
                Q.append((nr, nc, A[nr][nc]))
                break
        for a in A:
            print(a)
        break



        # 냄새 남아있는 부분 냄새 남은 시간 줄이기
        # for i in range(N):
        #     for j in range(N):
        #         if A[i][j][2] == 1:     # 남은 시간 1이었으면 빈 공간으로 만들어주기
        #             A[i][j] = 0
        #         elif 2 <= A[i][j][2] < K:   # 2 ~ K-1이면 한 시간씩 줄여주기
        #             A[i][j][2] -= 1
        time += 1
    return time

# 상하좌우
dr = (0, -1, 1, 0, 0)
dc = (0, 0, 0, -1, 1)

# main
# 맵 크기, 상어 수, 냄새 없어지는 시간
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
first_pos = list(map(int, input().split()))
Q = deque()
for r in range(N):
    for c in range(N):
        if A[r][c]:
            num = A[r][c]
            # 맵에 [상어 번호, 현재 방향, 냄새 남은 시간(K)] 표시
            A[r][c] = [num-1, first_pos[num-1]-1, K]
            Q.append((r, c, A[r][c]))
# print("맵 초기 상태")
# for a in A:
#     print(a)
# print("Q 초기 상태", Q)

# shark_dir : 상어의 현재 방향에 따른 방향의 우선순위
shark_dir = [[[] for _ in range(4)] for _ in range(M)]
for i in range(M):
    for j in range(4):
        shark_dir[i][j] = list(map(int, input().split()))
# for shark in shark_dir:
#     print(shark)
# print("상어 이동방향 우선순위")
# print(shark_dir)

print(bfs())