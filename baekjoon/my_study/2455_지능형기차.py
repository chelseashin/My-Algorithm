import sys
sys.stdin = open('2455_input.txt')

MAX = 0
passengers = 0
for _ in range(4):
    off, on = map(int, input().split())
    # print(off, on)
    passengers += on
    passengers -= off
    MAX = max(MAX, passengers)
print(MAX)