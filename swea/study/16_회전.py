import sys
sys.stdin = open("16_input.txt")

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    print("#{} {}".format(tc+1, arr[M % N]))