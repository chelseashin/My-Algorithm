import sys
sys.stdin = open('7568_input.txt')

N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
for height, weight in info:
    rank = 1
    for i, j in info:
        if height < i and weight < j:
            rank += 1
    print(rank, end=" ")