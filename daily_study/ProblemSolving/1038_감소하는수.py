# 나의 풀이

def dfs(depth, limit, temp):
    global cnt
    if depth == limit:
        cnt += 1
        # print(temp, cnt)
        if cnt == N:
            print(temp)
            exit()
        return
    for i in range(int(temp[-1])):
        dfs(depth+1, limit, temp+str(i))

# main
N = int(input())
cnt = 9
if N < 10:
    print(N)
    exit()
else:
    for k in range(1, 11):
        for n in range(1, 10):
            dfs(0, k, str(n))
print(-1)

# ========================================================

# def dfs(depth, limit, temp):
#     global cnt
#     if depth == limit:
#         cnt += 1
#         if cnt == N:
#             print(temp)
#             exit()
#         return
#     if temp == "":
#         for i in range(limit-1, 10):
#             dfs(depth+1, limit, temp+str(i))
#     else:
#         for i in range(int(temp[-1])):
#             if limit - len(temp) - 1 > i:
#                 continue
#             dfs(depth+1, limit, temp+str(i))
#
#
# # main
# N = int(input())
# cnt = -1
#
# for k in range(1, 11):
#     dfs(0, k, "")
# print(-1)