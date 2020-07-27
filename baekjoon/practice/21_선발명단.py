import sys
sys.stdin = open("21_input.txt")

# def dfs(depth, k):
#     if depth == 11:
#         print(result)
#         return
#     for i in range(k, 11):
#         visited[i] = 1
#         result.append(i)
#         dfs(depth+1, i+1)
#         visited[i] = 0
#         result.pop()
#
# C = int(input())
# arr = [list(map(int, input().split())) for _ in range(11)]
# visited = [0] * 11
# result = []
# dfs(0, 0)

# 순열함수
result = []
visited = [0] * 11
def dfs(depth):
    if depth == 11:
        print(result)
        return
    if depth == 3:
        result.append(0)
        dfs(depth + 1)
        result.pop()
    else:
        for i in range(1, 11):
            if visited[i]:
                continue
            result.append(i)
            visited[i] = 1
            dfs(depth + 1)
            result.pop()
            visited[i] = 0
dfs(0)
