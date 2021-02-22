# 23:15 start
# 23:39 시간초과.. DP로 접근해야 한다!
# 참고해보자 https://cagongman.tistory.com/18

import sys
input = sys.stdin.readline

def check(sr, sc, size):
    for i in range(sr, sr+size):
        for j in range(sc, sc+size):
            if A[i][j] == '0':
                return 0
    return size

# main
N, M = map(int, input().split())
A = [list(input().strip()) for _ in range(N)]

MAX = 0
for r in range(N):
    for c in range(M):
        for size in range(min(N-r, M-c), 0, -1):
            MAX = max(MAX, check(r, c, size))
print(MAX)