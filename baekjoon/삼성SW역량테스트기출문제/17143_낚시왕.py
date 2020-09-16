import sys
sys.stdin = open('17143_input.txt')

# 상 하 좌 우
dr = (0, -1, 1, 0, 0)
dc = (0, 0, 0, -1, 1)

# 방향 바꾸기
rev = (0, 2, 1, 4, 3)

def shark(sr, sc, speed, dir, size):

    for _ in speed:
        sr += dr[dir]
        sc += dc[dir]
        if not (0 <= sr < R and 0 <= sc < C):
            dir = rev[dir]
            sr += dr[dir]
            sc += dc[dir]
        # A에 값이 있을 때 크기 비교 해주기
        if A[sr][sc]:
            if A[sr][sc][2] > size:
                return A[sr][sc]
            else:
                A[sr][sc] = (speed, dir, size)
                return [sr, sc, speed, dir, size]


# main
R, C, M = map(int, input().split())
A = [[[] for _ in range(C)] for _ in range(R)]

catch = 0
movement = []
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    A[r-1][c-1].append((s, d, z))
    movement.append((r, c, s, d, z))
    # print(r, c, s, d, z)

for a in A:
    print(a)
print(movement)

for col in range(C):
    # 땅과 제일 가까운 상어 낚시
    for row in range(R):
        if A[row][col]:
            A[row][col] = []
            break
    # 상어 이동

    for i in range(len(movement)):
        r, c, s, d, z = movement
        movement[i] = shark(r, c, s, d, z)



    for a in A:
        print(a)
    print()

print(catch)