import sys
sys.stdin = open("1244_input.txt")



T = int(input())
for tc in range(T):
    S, N = input().split()
    S = list(map(int, list(S)))
    N = int(N)
    size = len(S)
    MAX = 0
    dfs(S, N, 0)