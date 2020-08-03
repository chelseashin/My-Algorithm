import sys
sys.stdin = open('5189_input.txt')

def dfs(start):
    global A, N, V, MIN, temp
    if sum(V) == N-1:
        temp += A[start][0]
        # 최소값 갱신
        if temp < MIN:
            MIN = temp
        temp -= A[start][0]
    for next in range(1, N):
        if V[next]:
            continue
        V[next] = 1
        temp += A[start][next]
        dfs(next)
        temp -= A[start][next]
        V[next] = 0

T = int(input())
for tc in range(T):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    V = [0] * N
    MIN = float('inf')
    temp = 0
    dfs(0)
    print("#{} {}".format(tc+1, MIN))