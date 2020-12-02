import sys
sys.stdin = open("2304_input.txt")

N = int(input())
L = []
for _ in range(N):
    r, c = map(int, input().split())
    print(r, c)