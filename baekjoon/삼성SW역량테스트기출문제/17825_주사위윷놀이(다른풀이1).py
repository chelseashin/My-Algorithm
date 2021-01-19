import sys
sys.stdin = open('17825_input.txt')
input = sys.stdin.readline

# 윷놀이판 A 만들기
# A : 다음 칸에 대한 인덱스, 도착에 해당하는 21은 해당 지점 반복
A = [0] * 33
for i in range(21):
    A[i] = i+1
A[21] = 21                  # 도착
A[22:25] = [23, 24, 30]     # 10에서 안으로 들어가는 경로의 인덱스
A[25:27] = [22, 24]         # 20에서 안으로
A[27:30] = [28, 29, 30]     # 30에서 안으로
A[30:33] = [31, 32, 20]
# print('A', A)
# print(A[21])
# print(A[5], A[10], A[15])

# 5, 10, 15번 인덱스에서 안쪽 다음 칸에 해당하는 인덱스를 연결
move_in = [0] * 16
move_in[5], move_in[10], move_in[15] = 22, 25, 27
print("move_in", move_in)
plus = [0] * 33     # 해당 칸에서 더해줄 숫자
for i in range(1, 21):
    plus[i] = i*2
plus[22:25] = [13, 16, 19]
plus[25:27] = [22, 24]
plus[27:30] = [28, 27, 26]
plus[30:33] = [25, 30, 35]
print('plus', plus)

def dfs(depth, score):
    global MAX
    if depth == 10:
        MAX = max(MAX, score)
        return

    for i in range(4):
        nx, x, move = chess[i], chess[i], dice[depth]

        if nx == 5 or nx == 10 or nx == 15:
            nx = move_in[nx]
            move -= 1

        if nx + move <= 21:     # 이동 후 위치가 도착지점보다 전이라면
            nx += move
        else:
            for _ in range(move):
                nx = A[nx]
        # 이동할 칸에 말이 있거나 이미 도착했을 경우
        if visited[nx] and nx != 21:
            continue

        visited[x], visited[nx], chess[i] = 0, 1, nx
        dfs(depth+1, score+plus[nx])
        visited[x], visited[nx], chess[i] = 1, 0, x

# main
dice = list(map(int, input().split()))
chess = [0] * 4     # 말의 위치
visited = [0] * 33

MAX = 0
dfs(0, 0)
print(MAX)