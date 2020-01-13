import sys
sys.stdin = open("18_input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    cards = list(map(int, input().split()))
