import sys
sys.stdin = open("6057_input.txt")

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    G = [[]]
    for _ in range(M):
        x, y = map(int, input().split())
