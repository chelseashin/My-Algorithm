import sys
sys.stdin = open('1520_input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
for a in A:
    print(a)