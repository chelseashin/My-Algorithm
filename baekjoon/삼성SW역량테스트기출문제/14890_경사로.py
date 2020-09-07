import sys
sys.stdin = open('14890_input.txt')

N, L = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
print(A)