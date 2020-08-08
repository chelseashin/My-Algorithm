# https://chldkato.tistory.com/14?category=876515
import sys
sys.stdin = open('2468_input.txt')

from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs(sr, sc):
    global rain, visited
    Q = deque([(sr, sc)])
    visited[sr][sc] = 1
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if A[nr][nc] <= rain:
                continue
            if visited[nr][nc]:
                continue
            visited[nr][nc] = 1
            Q.append((nr, nc))

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
safeArea = float('-inf')

# 비의 최대 양 결정
top = float('-inf')
for i in range(N):
    for j in range(N):
        if A[i][j] > top:
            top = A[i][j]

# 비의 양마다 안전영역 갯수 구하기
for rain in range(top+1):
    temp = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[i][j] > rain and visited[i][j] == 0:
                bfs(i, j)
                temp += 1
    if temp > safeArea:
        safeArea = temp

print(safeArea)