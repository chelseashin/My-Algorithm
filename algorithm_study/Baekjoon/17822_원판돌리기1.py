import sys
sys.stdin = open("17822_input.txt")

from collections import deque

# 원판 회전 함수
def rotate(X, D, K):
    global N, M, A
    for x in range(X-1, N, X):  # 회전하는 원판 X의 배수
        if D:  # 시계방향
            A[x].rotate(-K)
        else:  # 반시계방향
            A[x].rotate(K)
    return

# flag가 0일 때 호출됨
def control(A):
    global N, M
    plus = 0
    cnt = 0
    for i in range(N):
        for j in range(M):
            if A[i][j]:
                plus += A[i][j]
                cnt += 1
    avg = plus / cnt

    for i in range(N):
        for j in range(M):
            if A[i][j]:
                if A[i][j] > avg:
                    A[i][j] -= 1
                elif A[i][j] < avg:
                    A[i][j] += 1
    return

# 인접한 같은 수 지우기(dfs로 구현)
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def remove(sr, sc):
    global A, flag
    S = [(sr, sc)]
    while S:
        r, c = S.pop(-1)
        for i in range(4):
            nr = r + dr[i]
            nc = (c + dc[i] + M) % M
            if not (0 <= nr < N):
                continue
            if not A[nr][nc]:
                continue
            if A[r][c] != A[nr][nc]:
                continue
            flag = 1
            A[r][c] = 0
            A[nr][nc] = 0
            S.append((nr, nc))
    return

N, M, T = map(int, input().split())
A = [deque(map(int, input().split())) for _ in range(N)]

for _ in range(T):
    x, d, k = map(int, input().split())

    rotate(x, d, k)
    flag = 0
    for i in range(N):
        for j in range(M):
            if A[i][j]:
                remove(i, j)
        # 인접하면서 수가 같은 것이 없다.
    if flag == 0:
        control(A)
print(A)

# 최종 배열 A의 모든 원소 합
total = 0
for i in range(N):
    for j in range(M):
        if A[i][j]:
            total += A[i][j]
print(total)