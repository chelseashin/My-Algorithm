import sys
input = sys.stdin.readline

# 시간초과
def dfs(start, depth, temp):
    global MAX, cnt
    MAX = max(MAX, temp)
    cnt += 1
    if depth == N-start:
        return
    for idx in range(start+1, N):
        if A[start] > A[idx]:
            continue
        if A[start] < A[idx]:
            dfs(idx, depth+1, temp+A[idx])
        dfs(idx, depth+1, temp)

# main
N = int(input())
A = list(map(int, input().split()))

MAX = 0
cnt = 0
check = [0] * N
dfs(0, 0, A[0])
print(MAX)
# print(cnt)