import sys
sys.stdin = open("03_input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    numbers = str(input())
    new = [0] * 10
    for i in numbers:
        new[int(i)] += 1

    MAX = float("-inf")
    ans = 0
    for n in range(len(new)):
        if new[n] >= MAX:
            MAX = new[n]
            ans = n
    print("#{} {} {}".format(tc+1, ans, MAX))