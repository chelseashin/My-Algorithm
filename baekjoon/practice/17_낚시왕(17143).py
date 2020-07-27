import sys
sys.stdin = open('17_input.txt')

R, C, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
print(arr)