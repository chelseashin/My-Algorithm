import sys
sys.stdin = open("12100_input.txt")
input = sys.stdin.readline

# 틀린 풀이
# - 합치는 것은 한 번만 가능한데, 스택을 사용하면 여러 번 합치게 됨

def move(dir, temp):
    global MAX
    if dir == 0:    # 상
        for j in range(N):
            S = []
            for i in range(N):
                if board[i][j]:
                    if not S:
                        S.append(board[i][j])
                        board[i][j] = 0
                    else:
                        if S[-1] != board[i][j]:
                            S.append(board[i][j])
                            board[i][j] = 0
                        else:
                            # S.pop()
                            # S.append(2 * board[i][j])
                            S.append(2 * S.pop())
                            board[i][j] = 0
            # print(j, "번째 열", S, len(S))
            for k in range(len(S)):
                board[k][j] = S[k]
                MAX = max(MAX, S[k])

    elif dir == 1:    # 하
        for j in range(N):
            S = []
            for i in range(N-1, -1, -1):
                if board[i][j]:
                    if not S:
                        S.append(board[i][j])
                        board[i][j] = 0
                    else:
                        if S[-1] != board[i][j]:
                            S.append(board[i][j])
                            board[i][j] = 0
                        else:
                            # S.pop()
                            # S.append(2 * board[i][j])
                            S.append(2 * S.pop())
                            board[i][j] = 0
            # print(j, "번째 열", S, len(S))
            for k in range(len(S)):
                # print(k, S[k])
                board[N-k-1][j] = S[k]
                MAX = max(MAX, S[k])

    elif dir == 2:    # 좌
        for i in range(N):
            S = []
            for j in range(N):
                if board[i][j]:
                    if not S:
                        S.append(board[i][j])
                        board[i][j] = 0
                    else:
                        if S[-1] != board[i][j]:
                            S.append(board[i][j])
                            board[i][j] = 0
                        else:
                            # S.pop()
                            S.append(2 * S.pop())
                            board[i][j] = 0
            for k in range(len(S)):
                board[i][k] = S[k]
                MAX = max(MAX, S[k])

    elif dir == 3:    # 우
        for i in range(N):
            S = []
            for j in range(N-1, -1, -1):
                if board[i][j]:
                    if not S:
                        S.append(board[i][j])
                        board[i][j] = 0
                    else:
                        if S[-1] != board[i][j]:
                            S.append(board[i][j])
                            board[i][j] = 0
                        else:

                            S.append(2 * S.pop())
                            board[i][j] = 0

            for k in range(len(S)):
                board[i][N-k-1] = S[k]
                MAX = max(MAX, S[k])
    # if temp == 5:
    #     print(dir, MAX)
    #     for b in board:
    #         print(b)
    #     print()

def dfs(depth):
    global MAX, board
    if depth == 5:
        return
    B = [x[:] for x in board]
    for d in range(4):
        move(d, depth+1)
        dfs(depth + 1)
        board = [x[:] for x in B]

# main
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
for b in board:
    print(b)
MAX = 0
dfs(0)
print(MAX)

# Debugging
# move(3)
# print()
# for b in board:
#     print(b)
# move(1)
# print()
# for b in board:
#     print(b)
#
# move(3)
# print()
# for b in board:
#     print(b)
#
# move(1)
# print()
# for b in board:
#     print(b)