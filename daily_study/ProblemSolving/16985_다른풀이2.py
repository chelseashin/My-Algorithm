# 얘도 실패.. 으악 뭐 때문인지

from sys import stdin
input = stdin.readline
from collections import deque
from itertools import permutations, product

df = (0, 0, 0, 0, -1, 1)
dr = (-1, 1, 0, 0, 0, 0)
dc = (0, 0, -1, 1, 0, 0)

def checkMaze(newMaze):
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
            if newMaze[nf][nr][nc] == 0 or visited[nf][nr][nc]:
                continue
            visited[nf][nr][nc] = visited[f][r][c] + 1     # 방문 가능
            Q.append((nf, nr, nc))

# 몇 층인지, 방향
def checkDir(idx, dir):
    new = []    # 해당 층의 회전 후 상태
    if dir == 1:
        for c in range(4, -1, -1):
            col = []
            for r in range(4, -1, -1):
                col.append(maze[idx][r][c])
            new.append(col)
    
    elif dir == 2:
        for r in range(4, -1, -1):
            row = []
            for c in range(4, -1, -1):
                row.append(maze[idx][r][c])
            new.append(row)
    
    elif dir == 3:
        for c in range(4, -1, -1):
            col = []
            for r in range(5):
                col.append(maze[idx][r][c])
            new.append(col)
    return new

def makeNewMaze():
    
    for temp in product((0, 1, 2, 3), repeat=5):
        # print("temp", temp)
        newMaze = []
        for i in range(5):          # 5개 층
            if temp[i] == 0:        # 0: 회전 안 한 경우
                newMaze.append(A[i])   # 그대로 추가
                continue
            newMaze.append(checkDir(i, temp[i]))      # (해당 층 번호, 회전 횟수)

        if newMaze[0][0][0] and newMaze[4][4][4]:    # 입구/출구 들어갈 수 있는 경우에만 새 미로 확인
            checkMaze(newMaze)      # 목적지 도착할 수 있는지 확인

def solve():
    for perm in permutations((0, 1, 2, 3, 4)):
        for i in range(5):
            A[perm[i]] = maze[i]    # 5층 다른 방법으로 쌓기
        # print(perm, A)
        makeNewMaze()

# main
maze = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
A = [[[0] * 5 for _ in range(5)] for _ in range(5)]
result = float('inf')
solve()
if result == float('inf'):
    print(-1)
else:
    print(result)