import sys
sys.stdin = open('06_input.txt')

import itertools

# 2
# 4 0 0 0 1 1 1 0 0
# 0 0 0 0 0 0 0 0 0

N = int(input())
arr = []
for ining in range(N):
    arr.append(list(map(int, input().split())))
# print(arr)
max_score = 0
order = list(itertools.permutations(range(1, 9)))
for o in order:
    new = list(o)
    new = new[0:3] + [0] + new[3:]
    # print(new)
    score = 0
    for a in range(N):
        A = []
        for n in new:
            A.append(arr[a][n])
        # print(A)


    if score > max_score:
        max_score = score

print(max_score)


# 순열 함수 - DFS
# result = []
# visited = [0] * 9
# def dfs(depth):
#     if depth == 9:
#         print(result)
#         return
#     if depth == 3:
#         result.append(0)
#         dfs(depth + 1)
#         result.pop()
#     else:
#         for i in range(1, 9):
#             if visited[i]:
#                 continue
#             result.append(i)
#             visited[i] = 1
#             dfs(depth + 1)
#             result.pop()
#             visited[i] = 0
# dfs(0)