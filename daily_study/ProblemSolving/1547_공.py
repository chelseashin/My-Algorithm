from sys import stdin
input = stdin.readline

N = int(input())
cups = [1, 2, 3]
for _ in range(N):
    x, y = map(int, input().split())
    cups[x-1], cups[y-1] = cups[y-1], cups[x-1]
print(cups.index(1) + 1)