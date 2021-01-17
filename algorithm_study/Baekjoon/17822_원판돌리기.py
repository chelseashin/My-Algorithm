import sys
from collections import deque

# 원판 회전 함수
def rotate_plate(X, D, K):
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
    if cnt:
        avg = plus / cnt
    else:
        avg = 0
    # 이걸로 써도 무관함!
    # try:
    #     avg = plus / cnt
    # except:
    #     avg = 0
    for i in range(N):
        for j in range(M):
            if A[i][j] and avg != 0:
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
    flag2 = 0
    S = [(sr, sc)]
    key = A[sr][sc]
    A[sr][sc] = 0
    pr, pc = sr, sc
    while S:
        r, c = S.pop()
        for i in range(4):
            nr = r + dr[i]
            nc = (c + dc[i]) % M
            if not (0 <= nr < N):
                continue
            if not A[nr][nc]:
                continue
            if A[nr][nc] != key:
                continue
            flag = 1
            flag2 = 1
            A[nr][nc] = 0
            pr, pc = nr, nc
            S.append((nr, nc))
    if flag2 == 0:
        A[pr][pc] = key
    return


N, M, T = map(int, input().split())
A = [deque(map(int, input().split())) for _ in range(N)]
# print(A)
for _ in range(T):
    x, d, k = map(int, input().split())
    rotate_plate(x, d, k)
    flag = 0
    for i in range(N):
        for j in range(M):
            if A[i][j]:
                remove(i, j)
    # 인접하면서 수가 같은 것이 없다.
    if flag == 0:
        control(A)

# 최종 배열 A의 모든 원소 합
total = 0
for i in range(N):
    for j in range(M):
        if A[i][j]:
            total += A[i][j]
print(total)