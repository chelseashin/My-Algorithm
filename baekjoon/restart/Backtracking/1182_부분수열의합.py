import sys
sys.stdin = open('1182_input.txt')

N, S = map(int, input().split())
L = list(map(int, input().split()))
ans = 0

# backtracking 풀이
def backtracking(depth, tot):
    global ans
    if depth == N:
        if tot == S:
            return 1
        else:
            return 0
    ans = backtracking(depth+1, tot) + backtracking(depth+1, tot+L[depth])
    return ans

ans = backtracking(0, 0)

if S == 0:
    print(ans - 1)
else:
    print(ans)

# bfs(조합) 풀이
# def bfs(depth, k, cnt):
#     global ans
#     if depth == cnt:
#         temp = 0
#         for t in order:
#             temp += L[t]
#         if temp == S:
#             ans += 1
#         return
#     for i in range(k, N):
#         if visited[i]:
#             continue
#         visited[i] = 1
#         order.append(i)
#         bfs(depth+1, i+1, cnt)
#         order.pop()
#         visited[i] = 0
# visited = [0] * N
# for i in range(1, N+1):
#     order = []
#     visited = [0] * N
#     bfs(0, 0, i)
#
# print(ans)