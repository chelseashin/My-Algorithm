import sys
sys.stdin = open('17472_input.txt')

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
print(MAP)