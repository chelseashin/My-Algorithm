import sys
sys.stdin = open('20_input.txt')

N = int(input())
ingu = [list(map(int, input().split())) for _ in range(N)]
print(ingu)