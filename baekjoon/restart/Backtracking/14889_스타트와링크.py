import sys
sys.stdin = open('14889_input.txt')

def dfs():
    global MIN
    power = [0, 0]
    for i in range(N):
        for j in range(N):
            if team[i] == team[j]:
                power[team[i]] += player[i][j]
    if MIN > abs(power[0] - power[1]):
        MIN = abs(power[0] - power[1])

def comb(depth, k):
    half = N//2
    # 가지치기
    if MIN == 0:
        return
    if depth == N:
        return
    if k == half:
        # print(team)
        dfs()
        return
    team[depth] = 1
    comb(depth + 1, k+1)
    team[depth] = 0
    comb(depth + 1, k)

N = int(input())
player = [list(map(int, input().split())) for _ in range(N)]
MIN = float('inf')
team = [0] * N
comb(0, 0)
print(MIN)