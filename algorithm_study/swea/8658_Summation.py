import sys
sys.stdin = open("8658_input.txt")

T = int(input())
for tc in range(T):
    L = list(map(str, input().split()))
    MAX = float('-inf')
    MIN = float('inf')
    for num in L:
        s = 0
        for i in num:
            s += int(i)
        if s > MAX:
            MAX = s
        if s < MIN:
            MIN = s
    print("#{} {} {}".format(tc+1, MAX, MIN))