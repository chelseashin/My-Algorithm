import sys
sys.stdin = open('17822_input.txt')

# 성공
# 절대 어려운 문제가 아니다!
# 다음에 풀 땐 deque 말고 그냥 리스트로 풀어보자
# 옆으로는 벽이 없는 원통이기 때문에 nc 다룰 때 % M 해줌
# flag 가 무엇을 의미하는지 헷갈리지 말기
# 남은 값이 없으면 avg = 0

from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def remove(sr, sc):
    global A, flag
    f = 0
    S = [(sr, sc)]
    temp = A[sr][sc]
    while S:
        r, c = S.pop()
        for i in range(4):
            nr = r + dr[i]
            nc = (c + dc[i]) % M
            if not (0 <= nr < N):
                continue
            if not A[nr][nc]:
                continue
            if A[nr][nc] == temp:
                A[nr][nc] = 0
                S.append((nr, nc))
                f = 1
    if f:
        A[sr][sc] = 0
        flag = True
    return

def control(A):
    count = 0
    total = 0
    for i in range(N):
        for j in range(M):
            if A[i][j]:
                count += 1
                total += A[i][j]
    if count:
        avg = total / count
    else:
        avg = 0

    for i in range(N):
        for j in range(M):
            if A[i][j] and avg != 0:
                if A[i][j] > avg:
                    A[i][j] -= 1
                elif A[i][j] < avg:
                    A[i][j] += 1

# main
N, M, T = map(int, input().split())
A = [deque(map(int, input().split())) for _ in range(N)]

for _ in range(T):
    # 원판 돌리기
    x, d, k = map(int, input().split())
    for i in range(x-1, N, x):
        if d:
            A[i].rotate(-k)
        else:
            A[i].rotate(k)
    # 지우기
    flag = False
    for r in range(N):
        for c in range(M):
            if A[r][c]:
                remove(r, c)
    # 인접하면서 수가 같은 것이 없으면
    if not flag:
        control(A)

# 남은 값들의 합
ans = 0
for i in range(N):
    for j in range(M):
        if A[i][j]:
            ans += A[i][j]
print(ans)