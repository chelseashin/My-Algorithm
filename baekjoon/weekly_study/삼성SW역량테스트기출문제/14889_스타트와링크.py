import sys
sys.stdin = open("14889_input.txt")
input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
print(N, S)