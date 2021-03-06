import sys
sys.stdin = open('2112_input.txt')
from itertools import combinations

# 시간초과

def test(F):
    check = 0
    for c in range(W):
        cnt = 1
        temp = F[0][c]
        for r in range(1, D):
            if F[r][c] == temp:
                cnt += 1
            else:
                temp = F[r][c]
                cnt = 1
            if cnt >= K:
                check += 1
                break
        if (c+1) != check:
            return False
    return True

def dfs(depth, k):
    global MIN, flag
    if depth > MIN or flag or depth > K:
        return
    if depth == k:
        if test(film):
            flag = 1
            MIN = min(MIN, depth)
        return
    for c in comb:
        for i in range(2):
            if selected[c]:
                continue
            selected[c] = 1
            film[c] = drug[i]
            dfs(depth+1, k)
            film[c] = raw[c]
            selected[c] = 0

T = int(input())
for tc in range(T):
    D, W, K = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(D)]
    MIN = float('inf')

    if test(raw):
        MIN = 0

    else:
        film = [r[:] for r in raw]
        drug = [[0] * W, [1] * W]
        flag = 0
        for i in range(1, K+1):
            for comb in combinations(range(D), i):
                selected = [0] * D
                dfs(0, i)
                if flag: break
            if flag: break

    print("#{} {}".format(tc+1, MIN))