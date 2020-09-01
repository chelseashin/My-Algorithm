import sys
sys.stdin = open('17144_input.txt')

# 위쪽 청정기 : 상 우 하 좌
ur = (-1, 0, 1, 0)
uc = (0, 1, 0, -1)

# 아랫쪽 청정기 : 하 우 상 좌
dr = (1, 0, -1, 0)
dc = (0, 1, 0, -1)

# 공기 청정기 작동
def clean(new, cleaner):
    for i in range(2):
        # 윗 부분
        if i == 0:
            r, c = cleaner[i][0]-1, cleaner[i][1]
            dir = 0
            while dir < 4:
                nr = r + ur[dir]
                nc = c + uc[dir]
                if not (0 <= nr < cleaner[i][0]+1 and 0 <= nc < C):
                    dir += 1
                    continue
                if new[nr][nc] == -1:
                    new[r][c] = 0
                    break
                new[r][c] = new[nr][nc]
                r, c = nr, nc
        # 아랫 부분
        elif i == 1:
            r, c = cleaner[i][0]+1, cleaner[i][1]
            dir = 0
            while dir < 4:
                nr = r + dr[dir]
                nc = c + dc[dir]
                if not (cleaner[i][0] <= nr < R and 0 <= nc < C):
                    dir += 1
                    continue
                if new[nr][nc] == -1:
                    new[r][c] = 0
                    break
                new[r][c] = new[nr][nc]
                r, c = nr, nc

# 미세먼지 확산
def spread(A):
    new = [[0] * C for _ in range(R)]
    cleaner = []
    for r in range(R):
        for c in range(C):
            if A[r][c] == -1:
                new[r][c] = -1
                cleaner.append((r, c))
            elif A[r][c] > 0:
                pos = []
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if not (0 <= nr < R and 0 <= nc < C):
                        continue
                    if A[nr][nc] == -1:
                        continue
                    pos.append((nr, nc))
                new[r][c] += A[r][c] - len(pos) * (A[r][c] // 5)
                for pr, pc in pos:
                    new[pr][pc] += A[r][c] // 5
    clean(new, cleaner)
    return new

# main
R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]

for _ in range(T):
    A = spread(A)

# 남은 미세먼지 수
mise = 0
for i in range(R):
    for j in range(C):
        if A[i][j] >= 0:
            mise += A[i][j]
print(mise)