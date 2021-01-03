import sys
sys.stdin = open("14889_input.txt")
input = sys.stdin.readline

def NChooseK(n, k):
    numerator = 1
    denominator = 1
    k = min(n-k, k) #조합의 대칭성을 이용하여 더 적은 수의 연산을 하기 위해서입니다.
    for i in range(1, k+1):
        denominator *= i
        numerator *= n+1-i
    return numerator/denominator

def comb(depth, k):
    global MIN, half, cnt, finish
    if cnt >= finish:
        return
    if depth == half:
        # 최솟값 갱신
        power = [0, 0]
        for i in range(N):
            for j in range(N):
                if team[i] == team[j]:
                    power[team[i]] += S[i][j]
        MIN = min(MIN, abs(power[0]-power[1]))
        cnt += 1
        return
    for i in range(k, N):
        team[i] = 1
        comb(depth+1, i+1)
        team[i] = 0

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
half = N // 2
finish = NChooseK(N, half) / 2
MIN = float('inf')
team = [0] * N
comb(0, 0)
print(MIN)