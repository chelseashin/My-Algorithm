import sys
sys.stdin = open('1022_input.txt')
input = sys.stdin.readline

# 하, 우, 상, 좌
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

r1, c1, r2, c2 = map(int, input().split())
board = [[0] * (c2 - c1 + 1) for _ in range(r2 - r1 + 1)]
total = (r2 - r1 + 1) * (c2 - c1 + 1)

y, x = 0, 0
num = 1
cnt = 0     # 한 방향에서 움직이는 횟수
dis = 1    # 한 방향에서 움직여야 할 횟수
d = 0
# max_num = 0

while total > 0:
    if r1 <= y <= r2 and c1 <= x <= c2:
        total -= 1
        board[y-r1][x-c1] = num
        max_num = num
    num += 1
    cnt += 1
    
    y = y + dy[d]
    x = x + dx[d]
    
    if cnt == dis:
        cnt = 0
        d = (d + 3) % 4
        if d == 0 or d == 2:    # 왼쪽 또는 오른쪽 향하는 경우
            dis += 1

max_num_len = len(str(max([board[0][0], board[0][-1], board[-1][0], board[-1][-1]])))
for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        print(str(board[i][j]).rjust(max_num_len), end=" ")
    print()