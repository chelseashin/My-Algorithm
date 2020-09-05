import sys
sys.stdin = open('17779_input.txt')

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
print(A)