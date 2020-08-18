# 바킹독 - 재귀
# 연습문제1 - 거듭제곱

def func1(a, b, m):
    val = 1
    print(b)
    while b:

        val *= a
        b //= 2
        # b -= 1
    return val % m

# A, B, C = map(int, input().split())
# print(func1(A, B, C))
print('f', func1(10, 11, 12))

# print(pow(A, B, C))
# print(pow(10, 11, 12))

def func2(a, b, m):
    if b == 1:
        return a % m
    val = func2(a, b//2, m)
    if (b % 2 == 0):
        return val
    return val * a % m

print('f2', func2(10, 11, 12))

# 분할정복
# 시간복잡도 : O(logN)
def func3(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b % 2:
        return func3(a, b-1) * a
    else:
        half = func3(a, b//2)
        half %= C
        return half ** 2 % C
C = 12
print('f3', func3(10, 11) % 12)
