import sys
sys.stdin = open('2112_input.txt')

T = int(input())
for tc in range(T):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    MIN = 0

    print("#{} {}".format(tc+1, MIN))