import sys
sys.stdin = open('2115_input.txt')

T = int(input())
for tc in range(T):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]
    print(honey)