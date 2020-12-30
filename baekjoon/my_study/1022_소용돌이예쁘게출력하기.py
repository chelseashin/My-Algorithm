import sys
sys.stdin = open('1022_input.txt')
input = sys.stdin.readline

r1, c1, r2, c2 = map(int, input().split())
# print(r1, c1, r2, c2)

# 우 상 좌 하
dr = (0, -1, 0, 1)
dc = (1, 0, -1, 0)


A = [[0] * (c2 - c1 + 1) for _ in range(r2 - r1 + 1)]
total = (r2 - r1 + 1) * (c2 - c1 + 1)
# 시작점 표시
sr, sc = -1 * r1, -1 * c1
A[sr][sc] = 1
total -= 1
direction = 0
dis = 1
num = 1
max_value = 0
while total:
    for i in range(2):
        for j in range(dis):
            num += 1
            nr = sr + dr[direction]
            nc = sc + dc[direction]
            sr, sc = nr, nc
            # print(dis, j, num, '방향', direction, '현 위치', (nr, nc), total)
            if not total:
                break
            if not (0 <= nr < (r2 - r1 + 1) and 0 <= nc < (c2 - c1 + 1)):
                continue
            A[nr][nc] = num
            max_value = num
            total -= 1
        direction = (direction + 1) % 4
    dis += 1

# for a in A:
#     print(*a)
max_length = len(str(max_value))
for i in A:
    for j in i:
        print(str(j).rjust(max_length), end=" ")
    print()