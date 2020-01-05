# {1, 2, 3}을 포함하는 모든 순열을 생성하는 함수

# for i in range(1, 4):
#     for j in range(1, 4):
#         if i != j:
#             for k in range(1, 4):
#                 if k != i and k != j:
#                     print(i, j, k)


# 순열 공식 - 이것만 외우자!

def dfs(depth):
    if depth == M:
        print(*order)
        return
    for i in range(1, N+1):
        if visit[i] == 0:
            visit[i] = 1
            order.append(i)
            dfs(depth+1)
            order.pop()
            visit[i] = 0

N, M = map(int, input().split())
order = []
visit = [0] * (N+1)
dfs(0)