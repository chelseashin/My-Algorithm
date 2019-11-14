import sys
sys.stdin = open('20_input.txt')

def bfs(population):
    global result
    visited = [0] * N
    for i in range(len(selected)):
        if selected[i] == 1:
            q = [i]
            visited[i] = 1
            break
    while q:
        start = q.pop(0)
        for end in range(N):
            if visited[end] == 1:
                continue
            if selected[end] == 0:
                continue
            if arr[start][end] == 1:
                q.append(end)
                visited[end] = 1
    if sum(selected) != sum(visited):
        return

    visited = [0] * N
    for i in range(len(selected)):
        if selected[i] == 0:
            q = [i]
            visited[i] = 1
            break
    while q:
        start = q.pop(0)
        for end in range(N):
            if visited[end] == 1:
                continue
            if selected[end] == 1:
                continue
            if arr[start][end] == 1:
                q.append(end)
                visited[end] = 1
    if N - sum(selected) != sum(visited):
        return
    result = population
    return


def dfs(depth, k, goal):
    global result
    if depth == goal:
        A = 0
        for i in range(len(selected)):
            if selected[i] == 1:
                A += L[i]
        B = max_pop - A
        temp = abs(A - B)
        if temp < result:
            bfs(temp)
        return
    for i in range(k, N):
        selected[i] = 1
        dfs(depth + 1, i + 1, goal)
        selected[i] = 0

N = int(input())
L  = list(map(int, input().split()))
arr = [[0] * N for _ in range(N)]
max_pop = sum(L)
result = float('inf')

for n in range(N):
    info = list(map(int, input().split()))
    for m in info[1:]:
        arr[n][m-1] = 1
        arr[m-1][n] = 1

for i in range(1, N):
    selected = [0] * N
    dfs(0, 0, i)

if result == float('inf'):
    result = -1
print(result)