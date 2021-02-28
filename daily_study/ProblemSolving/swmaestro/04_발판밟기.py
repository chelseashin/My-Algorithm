# 나의 풀이
N = int(input())
A = list(map(int, input().split()))
maxCnt = 0
for x in range(3):
    visited = [0] * N
    visited[x] = 1
    while True:
        nx = x + A[x]
        if not visited[nx]:
            visited[nx] = visited[x] + 1
        else:
            maxCnt = max(maxCnt, visited[x] + 1)
            break
        x = nx
print(maxCnt)

# n = int(input())
# maxCnt = 0
# arr = list(map(int, input().split()))
# for i in range(3):
#     cnt = 0
#     visit = [0] * n
#     x = i
#     while 1:
#         visit[x] = 1
#         cnt += 1
#         nx = x + arr[x]
#         if visit[nx]:
#             maxCnt = max(maxCnt, cnt+1)
#             break
#         x = nx
# print(maxCnt)