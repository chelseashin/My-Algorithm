import sys
sys.stdin = open("1935_input.txt")

N = int(input())
S = input()
L = [int(input()) for _ in range(N)]
print(N, S, L)