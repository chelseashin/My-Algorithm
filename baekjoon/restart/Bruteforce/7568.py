import sys
sys.stdin = open('7568_input.txt')

def check(h, w):
    rank = 1
    for i, j in info:
        if h < i and w < j:
            rank += 1
    return rank

N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
for height, weight in info:
    print(check(height, weight), end=" ")