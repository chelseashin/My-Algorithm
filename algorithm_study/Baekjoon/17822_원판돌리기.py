# 실패한 코드 -- 비효율적임
import sys
sys.stdin = open("17822_input.txt")

from collections import deque

# 원판 회전 함수
def rotate(X, D, K):
    global N, M, A
    for x in range(X-1, N, X):  # 회전하는 원판 X의 배수
        if D:    # 시계방향
            A[x].rotate(-K)
        else:    # 반시계방향
            A[x].rotate(K)
    return

# 인접한 같은 수 지우기
def remove(A):
    flag = 0
    # 가로
    for i in range(N):
        S = []
        temp = 0
        for j in range(M):
            if len(S) == 0 and temp != A[i][j]:
                if A[i][j]:
                    S.append(A[i][j])
                    temp = S[-1]
                    # if temp == A[i][j]:
                    #     temp = S.pop(-1)
            else:
                if temp == A[i][j] and A[i][j]:
                    S.append(A[i][j])
                    temp = S.pop(-1)
                    A[i][j-1], A[i][j] = 0, 0
                    flag = 1
                else:
                    if temp != A[i][j]:
                        S.append(A[i][j])
                        temp = S[-1]

        if A[i][0] == A[i][-1]:
            A[i][0], A[i][-1] = 0, 0
            flag = 1

    # 세로
    for j in range(M):
        S = []
        temp = 0
        for i in range(N):
            if len(S) == 0 and temp != A[i][j]:
                if A[i][j]:
                    S.append(A[i][j])
                    temp = S[-1]
                    # if temp == A[i][j]:
                    #     temp = S.pop(-1)
            else:
                if temp == A[i][j] and A[i][j]:
                    S.append(A[i][j])
                    temp = S.pop(-1)
                    A[i][j-1], A[i][j] = 0, 0
                    flag = 1
                else:
                    if temp != A[i][j]:
                        S.append(A[i][j])
                        temp = S[-1]

    # 인접하면서 수가 같은 것이 없다.
    if not flag:
        control(A)
    return

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
            if A[i][j] > avg:
                A[i][j] -= 1
            elif A[i][j] < avg:
                A[i][j] += 1
    return

N, M, T = map(int, input().split())
A = [deque(map(int, input().split())) for _ in range(N)]

for _ in range(T):
    x, d, k = map(int, input().split())
    rotate(x, d, k)
    remove(A)

print(A)

# 최종 배열 A의 모든 원소 합
total = 0
for i in range(N):
    for j in range(M):
        if A[i][j]:
            total += A[i][j]
print(total)