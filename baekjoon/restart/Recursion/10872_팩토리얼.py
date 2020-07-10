N = 10
# N = int(input())
# ans = 1
# for i in range(1, N+1):
#     ans *= i

def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(N))