import sys
sys.stdin = open('17471_input.txt')
input = sys.stdin.readline
from collections import deque

# 올바른 구역 나누기인지 확인
def bfs():
    # 1인 것끼리 연결되어 있는지 확인
    Q = deque()
    visited = [0] * N
    for i in range(N):
        if selected[i]:
            Q.append(i)
            visited[i] = 1
            break
    while Q:
        s = Q.popleft()
        for e in range(N):
            if visited[e]:
                continue
            if not selected[e]:
                continue
            if G[s][e]:
                visited[e] = 1
                Q.append(e)
    if visited != selected:
        return False
    # 0인 것끼리 연결되어 있는지 확인
    Q.clear()
    visited = [1] * N
    for i in range(N):
        if not selected[i]:
            Q.append(i)
            visited[i] = 0
            break
    while Q:
        s = Q.popleft()
        for e in range(N):
            if selected[e]:
                continue
            if not visited[e]:
                continue
            if G[s][e]:
                Q.append(e)
                visited[e] = 0
    if visited != selected:
        return False
    return True


def comb(depth, k, goal):
    global result
    if depth == goal:
        # print(selected)
        if bfs():
            A, B = 0, 0
            for n in range(N):
                if selected[n]:
                    A += population[n]
                else:
                    B += population[n]
            result = min(result, abs(A-B))
        return
    for i in range(k, N):
        selected[i] = 1
        comb(depth+1, i+1, goal)
        selected[i] = 0

# main
N = int(input())
population = list(map(int, input().split()))
G = [[0] * N for _ in range(N)]
for i in range(N):
    for j in list(map(int, input().split()))[1:]:
        G[i][j-1] = 1

result = float('inf')
selected = [0] * N
for g in range(1, N//2+1):
    comb(0, 0, g)

if result == float('inf'):
    print(-1)
else:
    print(result)