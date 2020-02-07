import sys
sys.stdin = open("02_input.txt")

T = int(input())
K, N, M = map(int, input().split())
for tc in range(M):
    num = list(map(int, input().split()))
    print(num)