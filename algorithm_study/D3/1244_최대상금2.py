import sys
sys.stdin = open("1244_input.txt")

def dfs(N, L, I):
    global MAX
    # 종료 조건
    if N == 0:   # 자리 바꿀 수 있는 횟수
        L = int(''.join(map(str, L)))
        if MAX < L:
            MAX = L
        return

T = int(input())
for tc in range(T):
    S, N = input().split()
    S = list(map(int, list(S)))
    N = int(N)
    size = len(S)
    MAX = 0
    dfs(S, N, 0)

    print("#{} {}".format(tc+1, MAX))