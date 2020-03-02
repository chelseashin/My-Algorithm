import sys
sys.stdin = open('17135_input.txt')

N, M, D = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
print(A)