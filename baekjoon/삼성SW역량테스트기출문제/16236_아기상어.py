import sys
sys.stdin = open('16236_input.txt')

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
print(S)