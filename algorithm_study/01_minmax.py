import sys
sys.stdin = open("01_input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    MAX = float("-inf")
    MIN = float("inf")
    for n in numbers:
        if n < MIN:
            MIN = n
        if n > MAX:
            MAX = n
    print("#{} {}".format(tc+1, MAX-MIN))