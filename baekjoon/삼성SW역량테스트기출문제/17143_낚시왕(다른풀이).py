import sys
sys.stdin = open('17143_input.txt')

input = sys.stdin.readline

# 상 하 우 좌
dr = (0, -1, 1, 0, 0)
dc = (0, 0, 0, 1, -1)

# 방향 바꾸기
rev = (0, 2, 1, 4, 3)

def move():
    check = [[0] * C for _ in range(R)]
    temp = []
    cnt = 0
    for a in range(R):
        for b in range(C):
            if A[a][b]:
                cnt += 1
                speed, dir, size = A[a][b]
                A[a][b] = 0
                nr, nc = a, b
                for _ in range(speed):  # 속도만큼
                    nr += dr[dir]
                    nc += dc[dir]
                    if not (0 <= nr < R and 0 <= nc < C):
                        nr = nr-2*dr[dir]
                        nc = nc-2*dc[dir]
                        dir = rev[dir]
                if not check[nr][nc]:    # 없으면 새로 등록
                    temp.append((nr, nc))
                    check[nr][nc] = (speed, dir, size)
                else:   # 있으면 크기 비교
                    if check[nr][nc][2] < size:
                        check[nr][nc] = (speed, dir, size)
    for y, x in temp:
        A[y][x] = check[y][x]

# main
R, C, M = map(int, input().split())
if M == 0:
    print(0)
    exit()
A = [[0] * C for _ in range(R)]
for _ in range(M):
    r, c, speed, dir, size = map(int, input().split())
    A[r-1][c-1] = (speed, dir, size)
# print(A)

res = 0
for i in range(C):
    for j in range(R):
        if A[j][i]:
            res += A[j][i][2]
            A[j][i] = 0
            break
    move()
    # break
print(res)