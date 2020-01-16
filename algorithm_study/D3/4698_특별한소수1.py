import sys
sys.stdin = open("4698_input.txt")

def table(n):
    t = [0, 0] + [1] * (n-1)
    primes = []
    for i in range(2, n+1):
        if t[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                t[j] = 0
    return primes

def div(N):
    while N:
        c = N % 10
        if c == D:
            return False
        N = N // 10
    return True


primes = table(1000000)

T = int(input())
for tc in range(T):
    D, A, B = map(int, input().split())
    cnt = 0
    for i in range(len(primes)):
        if A <= primes[i] <= B:
            if not div(primes[i]):
                cnt += 1
        if primes[i] > B:
            break
    print("#{} {}".format(tc+1, cnt))