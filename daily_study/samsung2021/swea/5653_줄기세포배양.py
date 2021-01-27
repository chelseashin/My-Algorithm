import sys
sys.stdin = open("5653_input.txt")

# main
T = int(input())
for tc in range(T):
    N, M, K = map(int, input())
    raw = [list(map(int, input().split())) for _ in range(N)]


    print("#{} {}".format(tc+1, ))