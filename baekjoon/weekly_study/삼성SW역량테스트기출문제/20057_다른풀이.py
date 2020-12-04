import sys
sys.stdin = open("20057_input.txt")
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 참고 블로그
# https://m.blog.naver.com/pasdfq/222120109948

# 우 하 좌 상
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def dfs(r, c, d):
    visited[r][c] = 1
    for i in range(4):
        nr = r + dr[(d+i) % 4]
        nc = c + dc[(d+i) % 4]
        if not (0 <= nr < N and 0 <= nc < N):
            continue
        if visited[nr][nc]:
            continue
        path.append((r, c, (d+i+2) % 4))
        dfs(nr, nc, (d+i) % 4)
        break

# main
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
path = []
dfs(0, 0, 0)
path.reverse()
print(path)

# 비율 리스트
# 우 하 좌 상
ratio = [0, 0, [(-2, 0, 2), (-1, -1, 10), (-1, 0, 7), (-1, 1, 1),
                (0, -2, 5), (1, -1, 10), (1, 0, 7), (1, 1, 1), (2, 0, 2)], 0]

for i in range(4):
    ratio[(i+3) % 4] = [(i[1], -i[0], i[2]) for i in ratio[(i+2) % 4]]

total = 0
for i in range(N):
    for j in range(N):
        total += A[i][j]
# 토네이도 시전
for (r, c, d) in path:
    sand = A[r][c]
    # 모래 날리기
    # (sr, sc) 방향으로 p 퍼센트 만큼 이동
    for (sr, sc, p) in ratio[d]:
        nr = r + sr
        nc = c + sc
        A[r][c] -= sand * p // 100
        if not (0 <= nr < N and 0 <= nc < N):
            continue
        A[nr][nc] += sand * p // 100

    # 알파
    nr = r + dr[d]
    nc = c + dc[d]
    if (0 <= nr < N and 0 <= nc < N):
        A[nr][nc] += A[r][c]
    A[r][c] = 0

temp = 0
for i in range(N):
    for j in range(N):
        temp += A[i][j]

print(total - temp)