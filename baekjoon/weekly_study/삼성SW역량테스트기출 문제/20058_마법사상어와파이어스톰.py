import sys
sys.stdin = open("20058_input.txt")

# main
N, Q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(2 ** N)]
L = list(map(int, input().split()))
