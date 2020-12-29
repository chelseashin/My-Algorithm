import sys
sys.stdin = open('1022_input.txt')
input = sys.stdin.readline

# 우 상 좌 하
d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
r1, c1, r2, c2 = map(int, input().split())
arr = [[0] * (c2-c1+1) for _ in range(r2-r1+1)]
max_level = max(abs(r1), abs(c1), abs(r2), abs(c2))
r, c = 0, 0
cnt = 1
max_cnt = (max_level*2 + 1) ** 2
dist = 0
max_value = 0
i = 0

while cnt <= max_cnt:
    if d[i][0]: dist += 1
    for _ in range(dist):
        if r1 <= r <= r2 and c1 <= c <= c2:
            arr[r-r1][c-c1] = cnt
            max_value = cnt
        cnt += 1
        c += d[i][0]
        r += d[i][1]

    i = (i + 1) % 4

max_length = len(str(max_value))
for i in arr:
    for j in i:
        print(str(j).rjust(max_length), end=" ")
    print()