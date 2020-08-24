import sys
sys.stdin = open('14889_input.txt')

def score(team):
    global MIN
    power = [0, 0]
    for i in range(N):
        for j in range(N):
            if team[i] == team[j]:
                power[team[i]] += player[i][j]
    # print(power)
    MIN = min(MIN, abs(power[0]-power[1]))

def comb(depth, k):
    global MIN
    if MIN == 0:
        return
    if depth == N:
        return
    if k == N//2:
        # print(result)
        score(result)
        return
    result[depth] = 1
    comb(depth+1, k+1)
    result[depth] = 0
    comb(depth+1, k)

# main
N = int(input())
player = [list(map(int, input().split())) for _ in range(N)]
MIN = float('inf')

result = [0] * N
comb(0, 0)
print(MIN)