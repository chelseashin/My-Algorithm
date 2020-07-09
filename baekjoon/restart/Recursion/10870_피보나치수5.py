N = 5
# N = int(input())
# fibonacci(n-1) + fibonacci(n-2)
def fibonacci(n):
    if n >= 2 and len(memo) <= n:
        memo.append(fibonacci(n - 1) + fibonacci(n - 2))
    return memo[n]

memo = [0, 1]
# print(fibonacci(N))


def fibo2(n) :
    f = [0, 1]
    for i in range(2, n + 1) :
        f.append(f[i-1] + f[i-2])
    return f[n]

print(fibo2(10))