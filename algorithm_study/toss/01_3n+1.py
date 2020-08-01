# runtime error
# input = "10 30 0"    # 112
input = "100 200 1"  # 125

L = list(map(int, input.split()))
a, b, c = L[0], L[1], L[2]
answer = float('-inf')

for n in range(a, b+1):
    temp = 1
    while n != 1:
        temp += 1
        if n%2:  # 홀수
            if n * 3 + 1 > b / 3 and c > 0:
                n = 3 * n + 1
                n += 10
                c -= 1
            else:
                n = 3 * n + 1
        else:    # 짝수
            n //= 2
    # print(temp)
    if answer < temp:
        answer = temp
print(answer)