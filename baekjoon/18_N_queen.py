import sys
sys.stdin = open('18_input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    board = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    dfs(0)
    print("#{} {}".format(tc+1, board))