import sys
sys.stdin = open("17281_input.txt")

N = int(input())
for _ in range(N):
    result = list(map(int, input().split()))
    print(result)