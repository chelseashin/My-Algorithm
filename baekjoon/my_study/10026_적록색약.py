import sys
sys.stdin = open("10026_input.txt")

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dfs(sr, sc, arr):
    temp = arr[sr][sc]
    S = [(sr, sc)]
    arr[sr][sc] = 0
    while S:
        r, c = S.pop()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if arr[nr][nc] == temp:
                S.append((nr, nc))
                arr[nr][nc] = 0

        # print(S)

# main
N = int(input())
A, B = [], []
for i in range(N):
    A.append(list(input()))
    b = []
    for j in range(N):
        if A[i][j] == "G":
            b.append("R")
        else:
            b.append(A[i][j])
    B.append(b)

cnt1, cnt2 = 0, 0
for r in range(N):
    for c in range(N):
        if A[r][c]:
            dfs(r, c, A)
            cnt1 += 1
        if B[r][c]:
            dfs(r, c, B)
            cnt2 += 1

print(cnt1, cnt2)