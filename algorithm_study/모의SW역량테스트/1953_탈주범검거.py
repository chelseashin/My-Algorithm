import sys
sys.stdin = open("1953_input.txt")

T = int(input())
for tc in range(T):
    N, M, R, C, L = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    print("#{} {}".format(tc+1, ans))