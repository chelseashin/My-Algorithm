import sys
sys.stdin = open("20_input.txt")

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    L = list(map(int, input().split()))
    print("#{} {}".format(tc+1, L[M % N]))