import sys
sys.stdin = open("17136_input.txt")
# 우, 하
dr = (1, 0)
dc = (0, 1)

def dfs(sr, sc):
    global paper, N, rdis
    S = [(sr, sc)]
    paper[sr][sc] = 0
    rdis = 0
    while S:
        r, c = S.pop()

        for i in range(2):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if not paper[nr][nc]:
                continue
            S.append((nr, nc))
            paper[nr][nc] = 0
    return

    # for i in range(5, 0, -1):


N = 10
paper = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N  for _ in range(N)]
MIN = float('inf')
cnt = 0
for i in range(N):
    for j in range(N):
        if paper[i][j]:
            dfs(i, j)
            cnt += 1
            # if cnt < MIN:
            #     MIN = cnt

print(cnt)