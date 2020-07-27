import sys
sys.stdin = open('2606_input.txt')

# def dfs(start):
#     global cnt
#     visited[start] = 1
#     for i in range(1, C+1):
#         if visited[i] == 0 and G[start][i] == 1:
#             cnt += 1
#             dfs(i)

def bfs(start):
    global cnt
    Q = [start]
    visited[start] = 1
    while Q:
        s = Q.pop(0)
        for i in range(1, C+1):
            if visited[i] == 0 and G[s][i] == 1:
                visited[i] = 1
                cnt += 1
                Q.append(i)

C = int(input())
N = int(input())
G = [[0] * (C+1) for _ in range(C+1)]
for _ in range(N):
    s, g = map(int, input().split())
    G[s][g] = 1
    G[g][s] = 1
# print(G)
cnt = 0
visited = [0] * (C+1)
# dfs(1)

bfs(1)
print(visited)
print(cnt)