import sys
sys.stdin = open('1987_input.txt')

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dfs(r, c, cnt):
    global MAX
    # if MAX < cnt:
    #     MAX = cnt
    MAX = max(MAX, cnt)
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if not (0 <= nr < R and 0 <= nc < C):
            continue
        if alphabet[ord(A[nr][nc])-65]:
            continue
        alphabet[ord(A[nr][nc])-65] = 1
        dfs(nr, nc, cnt+1)
        alphabet[ord(A[nr][nc])-65] = 0

# main
R, C = map(int, input().split())
A = [list(input()) for _ in range(R)]
alphabet = [0] * 26
alphabet[ord(A[0][0]) - 65] = 1
MAX = 0
dfs(0, 0, 1)
print(MAX)