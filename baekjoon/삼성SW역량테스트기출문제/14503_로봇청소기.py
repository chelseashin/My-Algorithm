import sys
sys.stdin = open('14503_input.txt')

N, M = map(int, input().split())
r, c, d = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]
print(space)