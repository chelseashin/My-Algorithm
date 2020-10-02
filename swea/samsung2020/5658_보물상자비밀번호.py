import sys
sys.stdin = open('5658_input.txt')

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    S = input()
    num = N//4
    numbers = set()
    for _ in range(num):
        for i in range(0, N, num):
            temp = S[i:i+num]
            numbers.add(temp)
        S = S[-1] + S[:-1]

    L = [int(n, 16) for n in numbers]
    print("#{} {}".format(tc+1, sorted(L, reverse=True)[K-1]))

    # 1 503
    # 2 55541
    # 3 334454
    # 4 5667473
    # 5 182189737