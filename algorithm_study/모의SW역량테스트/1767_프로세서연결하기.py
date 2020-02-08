import sys
sys.stdin = open("1767_input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    raw = [list(map(int, input().split())) for _ in range(N)]
    print(raw)