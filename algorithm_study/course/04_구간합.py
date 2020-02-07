import sys
sys.stdin = open("04_input.txt")

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    MAX = float('-inf')
    MIN = float('inf')
    for i in range(N-M+1):
        SUM = 0
        for n in range(M):
            SUM += numbers[i+n]
        if SUM > MAX:
            MAX = SUM
        if SUM < MIN:
            MIN = SUM
    print("#{} {}".format(tc+1, MAX-MIN))