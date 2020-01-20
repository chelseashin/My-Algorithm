import sys
sys.stdin = open("14501_input.txt")

def dfs(s, temp):
    global D, N, MAX
    if s > N:
        return
    if temp > MAX:
        MAX = temp
    for i in range(s + D[s][0], N):
        if D[i][0] <= N - i:
            dfs(i, temp + D[i][1])
        else:
            dfs(i, temp)

N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]
MAX = 0
# dfs(0, 0)
for i in range(N):
    if D[i][0] <= N-i:
        dfs(i, D[i][1])
print(MAX)