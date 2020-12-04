import sys
from collections import deque
sys.stdin = open("20057_input.txt")
input = sys.stdin.readline

# 우 하 좌 상
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

# main
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

before = 0
for i in range(N):
    for j in range(N):
        before += A[i][j]

visited = [[0] * N for _ in range(N)]
visited[0][0] = 1
path = deque([(0, 0, 2)])
dir = 0
r, c = 0, 0
cnt = 0
while True:
    nr = r + dr[dir]
    nc = c + dc[dir]
    if not (0 <= nr < N and 0 <= nc < N) or visited[nr][nc]:
        # 방향 바꾸기
        dir = (dir + 1) % 4
        continue
    visited[nr][nc] = 1
    path.appendleft((nr, nc, (dir+2) % 4))
    r, c = nr, nc
    if (nr, nc) == (N//2, N//2):
        break
print(path)

# y 기준 날리는 모래 (위치, 비율) 리스트
weight = (0.01, 0.01, 0.07, 0.07, 0.02, 0.02, 0.1, 0.1, 0.05)
# 좌 하 우 상
move = [[(-1, 1), (1, 1), (-1, 0), (1, 0), (-2, 0), (2, 0), (-1, -1), (1, -1), (0, -2)],
        [(-1, -1), (-1, 1), (0, -1), (0, 1), (0, -2), (0, 2), (1, -1), (1, 1), (2, 0)],
        [(-1, -1), (1, -1), (-1, 0), (1, 0), (-2, 0), (2, 0), (-1, 1), (1, 1), (0, 2)],
        [(1, -1), (1, 1), (0, -1), (0, 1), (0, -2), (0, 2), (-1, -1), (-1, 1), (-2, 0)]]

for a in A:
    print(a)

# 토네이도 시전
amount = 0
for r, c, d in path:
    if A[r][c]:     # 값이 있을 때
        sand = A[r][c]
        for i in range(9):
            nr = r + move[d][i][0]
            nc = c + move[d][i][1]
            # 격자 밖으로 나간 경우
            if not (0 <= nr < N and 0 <= nc < N):
                amount += int(sand * weight[i])
                continue
            # 그렇지 않으면 모래 이동
            A[nr][nc] += int(sand * weight[i])
            A[r][c] -= int(sand * weight[i])
            print(weight[i], move[d][i], "=>", (nr, nc))
        print(sand, (r, c), d)
        for a in A:
            print(a)
        break

print("amount :", amount)


later = 0
for i in range(N):
    for j in range(N):
        later += A[i][j]
print(later)

print(before - later)
print(amount)