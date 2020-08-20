# 순열 - 순서 중요
# def perm(depth):
#     if depth == M:
#         print(*order)
#         return
#     for i in range(1, N+1):
#         if not visited[i]:
#             visited[i] = 1
#             order.append(i)
#             perm(depth+1)
#             order.pop()
#             visited[i] = 0
#
# N, M = 5, 3
# # N, M = map(int, input().split())
# order = []
# visited = [0] * (N+1)
# perm(0)

# itertools 사용
# from itertools import permutations
# N, M = map(int, input().split())
# for x in list(permutations(range(1, N+1), M)):
#     print(*x)

# def perm(depth):
#     if depth == 6:
#         print(order)
#         return
#     for i in [0, 1]:
#         if visited[i] != 4:
#             visited[i] += 1
#             order.append(i)
#             perm(depth+1)
#             order.pop()
#             visited[i] -= 1


def perm(depth):
    if depth == M:
        print(*order)
        return
    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = 1
        order[depth] = i
        perm(depth+1)
        order[depth] = 0
        visited[i] = 0


N, M = 4, 3
# N, M = map(int, input().split())
order = [0] * M
visited = [0] * (N+1)
perm(0)