import sys
sys.stdin = open('7569_input.txt')

M, N, H = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
print(box)