import sys
input = sys.stdin.readline

def dfs(depth, k, temp):
    global result
    if temp > M:    # 가지치기
        return
    if depth == 3:
        if temp <= M:
            result = max(result, temp)
        return
    for i in range(k, N):
        if check[i]:
            continue
        check[i] = 1
        dfs(depth+1, i+1, temp + cards[i])
        check[i] = 0

N, M = map(int, input().split())
cards = list(map(int, input().split()))

result = 0

# 방법 1 - backtracking
check = [0] * N
dfs(0, 0, 0)
print(result)

# 방법 2 - 3중 for문
# for i in range(N-2):
#     for j in range(i+1, N-1):
#         for k in range(j+1, N):
#             temp = cards[i] + cards[j] + cards[k]
#             if temp <= M:
#                 result = max(result, temp)
# print(result)

