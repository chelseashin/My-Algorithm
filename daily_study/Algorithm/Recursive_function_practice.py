def multiple(N):
    if N <= 1:
        return N
    return N * multiple(N-1)

# def multiple(N):
#     temp = 1
#     for i in range(1, N+1):
#         temp *= i
#     return temp

# print(multiple(5))

import random

def sum_list(data):
    if len(data) <= 1:
        return data[0]
    return data[0] + sum_list(data[1:])

data = random.sample(range(100), 10)
# print(data)
# print(sum_list(data))

def palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False

# print(palindrome("level"))

def func(N):
    print(N)
    if N == 1:
        return N
    if N % 2:
        return func(N * 3 + 1)
    else:
        return func(N // 2)

# print()
# func(3)

def func1(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    elif N == 3:
        return 4

    return func1(N-1) + func1(N-2) + func1(N-3)

print(func1(5))
