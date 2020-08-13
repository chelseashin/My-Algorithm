import sys
sys.stdin = open('17471_input.txt')

from collections import deque

def bfs():
    # selected에서 1인 것 나누어지는지 조사
    Q = deque()
    visited = [0] * N
    for i in range(N):
        if selected[i] == 1:
            Q.append(i)
            visited[i] = 1
            break
    while Q:
        start = Q.popleft()
        for end in range(N):
            if visited[end] == 1:
                continue
            if selected[end] == 0:
                continue
            if G[start][end]:
                visited[end] = 1
                Q.append(end)
    if visited != selected:
        return False
    Q.clear()
    visited = [1] * N

    # selected에서 0인 것 나누어지는지 조사
    for i in range(N):
        if selected[i] == 0:
            Q.append(i)
            visited[i] = 0
            break
    while Q:
        s = Q.popleft()
        for end in range(N):
            if visited[end] == 0:
                continue
            if selected[end] == 1:
                continue
            if G[s][end]:
                visited[end] = 0
                Q.append(end)
    if selected != visited:
        return False
    return True

# 0과 1로 구역 나누기
def dfs(depth, k, goal):
    global MIN
    if depth == goal:
        # print(selected)
        if bfs():
            A = 0
            for i in range(N):
                if selected[i]:  # 1일 때
                    A += population[i]
            B = total_population - A
            if MIN > abs(A - B):
                MIN = abs(A - B)
        return
    for i in range(k, N):
        selected[i] = 1
        dfs(depth+1, i+1, goal)
        selected[i] = 0

# main
N = int(input())
population = list(map(int, input().split()))
G = [[0] * (N) for _ in range(N)]
for i in range(N):
    for j in list(map(int, input().split()))[1:]:
        G[i][j-1] = 1

total_population = sum(population)
MIN = float('inf')

# 각 선거구는 적어도 하나의 구역을 포함해야하기 때문에, 1부터 돌리기
for i in range(1, N):
    selected = [0] * N
    dfs(0, 0, i)

if MIN == float('inf'):
    print(-1)
else:
    print(MIN)