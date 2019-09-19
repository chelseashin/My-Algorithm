import sys
sys.stdin = open('19_input.txt')

N = int(input())
arr = list(input() for _ in range(N))
print(arr)