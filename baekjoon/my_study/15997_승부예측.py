import sys
sys.stdin = open("15997_input.txt")

countries = list(input().split())
for _ in range(6):
    A, B, W, D, L = map(str, input().split())
    print(A, B, W, B, L)