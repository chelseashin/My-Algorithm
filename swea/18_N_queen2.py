import sys
sys.stdin = open('18_input.txt')

def dfs(depth):
    global board, visited, N, count
    if depth == N:
        count += 1
        return
    for i in range(N):
        if visited[i]:
            continue
        # 대각선 검사
        for r, c in result:
            if abs(r - depth) == abs(c - i):
                break
        else:
            visited[i] = 1
            result.append((depth, i))
            dfs(depth + 1)
            visited[i] = 0
            result.pop()

T = int(input())
for tc in range(T):
    N = int(input())
    board = [[0] * N for _ in range(N)]
    visited = [0] * N
    result = []
    count = 0
    dfs(0)

    print("#{} {}".format(tc+1, count))