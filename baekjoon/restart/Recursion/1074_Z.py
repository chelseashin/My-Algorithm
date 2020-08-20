N, r, c = 3, 7, 7
# N, r, c = map(int, input().split())

def func(n, r, c):
    if n == 0:
        return 0
    half = 2**(n-1)
    # print(half)
    if (r < half and c < half):     # 1사분면
        return func(n-1, r, c)
    if (r < half and c >= half):    # 2사분면
        return half*half + func(n-1, r, c-half)
    if (r >= half and c < half):    # 3사분면
        return 2*half*half + func(n-1, r-half, c)
    return 3*half*half + func(n-1, r-half, c-half)      # 4사분면

print(func(N, r, c))