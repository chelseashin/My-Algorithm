import sys
input = sys.stdin.readline

# Brute Force

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dfs(depth, r, c, temp):
    global S
    if depth == 5:
        S.add(temp)
        return

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < 5 and 0 <= nc < 5:
            dfs(depth+1, nr, nc, temp+str(A[nr][nc]))

# main
A = [list(map(int, input().split())) for _ in range(5)]
S = set()       # 중복 제거
for i in range(5):
    for j in range(5):
        dfs(0, i, j, str(A[i][j]))
print(len(S))