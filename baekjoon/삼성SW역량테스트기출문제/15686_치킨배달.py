import sys
sys.stdin = open('15686_input.txt')

def comb(depth, k):
    if depth == M:
        print(selected)
        return
    for i in range(k, C):
        selected[i] = 1
        comb(depth+1, i+1)
        selected[i] = 0

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
print(M, city)

chicken = []
C = 0
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken.append((i, j))
            C += 1
print(C, chicken)

selected = [0] * C
comb(0, 0)