import sys
sys.stdin = open("13_input.txt")

def dfs(depth, total):
    global arr, Min, visited, N
    if depth == N:
        if Min > total:
            Min = total
        return
    # 가지치기
    if total >= Min:
        return
    for i in range(N):
        if visited[i] == 1:
            continue
        visited[i] = 1
        dfs(depth+1, total + arr[depth][i])
        visited[i] = 0

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    Min = float('inf')
    # depth와 total 둘다 0부터 시작
    dfs(0, 0)

    print("#{} {}".format(tc+1, Min))