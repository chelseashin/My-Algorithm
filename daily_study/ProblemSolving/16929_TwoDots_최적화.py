from sys import stdin
input = stdin.readline

# 하 우 상 좌
dr = (1, 0, -1, 0)
dc = (0, 1, 0, -1)

def dfs(r, c, char, br, bc):
    if check[r][c]:
        print("Yes")
        exit()
    
    check[r][c] = 1     # 방문 표시
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        # 벽이거나 문자 다르면 
        if not (0 <= nr < R and 0 <= nc < C) or board[nr][nc] != char:
            continue
        if (nr, nc) == (br, bc):    # 이전 위치와 같은 위치면 
            continue
        dfs(nr, nc, char, r, c)

# main
R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
check = [[0] * C for _ in range(R)]
for sr in range(R):
    for sc in range(C):
        if not check[sr][sc]:
            dfs(sr, sc, board[sr][sc], -1, -1)
print("No")