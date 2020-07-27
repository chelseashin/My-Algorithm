# 실패 코드

import sys
sys.stdin = open('18_input.txt')

def dfs(depth):
    global board, visited, N, count
    if depth == N:
        count += 1
        return

    # 열 관리
    for i in range(N):
        # visited[depth]의 모든 열이 다 차있는 경우
        if visited[depth][i]:
            continue
        for j in range(N):
            visited[depth][j] += 1    # 가로 채우기
            visited[j][i] += 1        # 세로 채우기
            # 대각선 - 오른쪽 대각선(/), 왼쪽 대각선(\)
            # visited[depth+j][i+j]
            if not (0 <= depth + j < N and 0 <= i+j < N):    # 벽이면
                continue
            visited[depth+j][i+j] += 1
            visited[depth-j][i+j] += 1
            if not (0 <= depth - j < N and 0 <= i-j < N):
                continue
            visited[depth+j][i-j] += 1
            visited[depth-j][i-j] += 1

            dfs(depth + 1)




T = int(input())
for tc in range(T):
    N = int(input())
    board = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    count = 0
    dfs(0)

    print("#{} {}".format(tc+1, count))