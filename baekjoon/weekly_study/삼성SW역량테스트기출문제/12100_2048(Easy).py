import sys
sys.stdin = open("12100_input.txt")
input = sys.stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def move(dir):
    if dir == 0:    # 상
        for i in range(N):

            for j in range(N):


def dfs(depth):
    global MAX, board
    if depth == 5:
        # 최댓값 갱신
        return

    B = [x[:] for x in board]
    for d in range(4):
        move(d)
        dfs(depth + 1)
        board = [x[:] for x in B]

# main
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
for b in board:
    print(b)
MAX = 0
dfs(0)