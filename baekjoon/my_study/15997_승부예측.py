import sys
sys.stdin = open("15997_input.txt")

# 실력 연마 후 다시 오자..
# https://qrlagusdn.tistory.com/78

names = list(input().split())
countries = dict()
for name in names:
    countries[name] = 0
print(countries)
for _ in range(6):
    A, B, W, D, L = map(str, input().split())
    print(A, B, W, D, L)
    if W > L:
        countries[A] += 3
    elif W < L:
        countries[B] += 3
    else:
        countries[A] += 1
        countries[B] += 1
    # countries[A]
    # countries[B]
    print(countries)

print(sorted(countries.items(), key=lambda x:x[1], reverse=True))