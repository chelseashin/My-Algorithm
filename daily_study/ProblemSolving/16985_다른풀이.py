from sys import stdin
input = stdin.readline
from collections import deque
from itertools import permutations

df = (0, 0, 0, 0, -1, 1)
dr = (-1, 1, 0, 0, 0, 0)
dc = (0, 0, -1, 1, 0, 0)

def checkMaze():
    global result
    visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = 1    # 시작 층, 행, 열 위치 표시
    Q = deque([(0, 0, 0)])
    while Q:
        f, r, c = Q.popleft()
        if (f, r, c) == (4, 4, 4):      # 목적지 도착
            result = min(result, visited[f][r][c] - 1)
            if result == 12:
                print(12)
                exit()
            return

        for d in range(6):
            nf = f + df[d]
            nr = r + dr[d]
            nc = c + dc[d]
            # 범위 밖이거나
            if not (0 <= nf < 5 and 0 <= nr < 5 and 0 <= nc < 5):
                continue
            # 갈 수 없는 곳이거나 이미 방문한 곳이면
            if A[nf][nr][nc] == 0 or visited[nf][nr][nc]:
                continue
            visited[nf][nr][nc] = visited[f][r][c] + 1     # 방문 가능
            Q.append((nf, nr, nc))

# 90도로 k번 회전
def rotate(k):
    temp = [[0] * 5 for _ in range(5)]
    for r in range(5):
        for c in range(5):
            temp[c][4-r] = A[k][r][c]
    A[k] = temp

# 층별로 돌리기
def turnMaze(cnt):
    if cnt == 5:
        if A[0][0][0] and A[4][4][4]:
            checkMaze()   # 정상 탈출 가능한지 확인
        return

    for i in range(4):  # 회전 방법 4가지
        if A[0][0][0]:
            turnMaze(cnt+1)
        rotate(cnt)

def solve():
    for perm in permutations((0, 1, 2, 3, 4)):
        for i in range(5):
            A[perm[i]] = maze[i]    # 5층 다른 방법으로 쌓기
        # print(perm, A)
        turnMaze(0)

# main
maze = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
A = [[[0] * 5 for _ in range(5)] for _ in range(5)]
result = float('inf')
solve()
if result == float('inf'):
    print(-1)
else:
    print(result)