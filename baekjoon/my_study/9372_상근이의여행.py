import sys
sys.stdin = open('9372_input.txt')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    for _ in range(M):
        a, b = map(int, input().split())
        print(a, b)