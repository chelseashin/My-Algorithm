import sys
sys.stdin = open('04_input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    # print(L)

    D = {i:L.count(i) for i in set(L)}
    Max = float('-inf')
    answer = 0
    for key, value in D.items():
        if Max < value:
            Max = value
            answer = key

    print("#{} {}".format(tc+1, answer))