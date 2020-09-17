import sys
sys.stdin = open('13460_input.txt')
input = sys.stdin.readline

# main
N, M = map(int, input().split())
B = [input()[:M] for _ in range(N)]
print(B)