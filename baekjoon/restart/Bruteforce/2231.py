import sys
sys.stdin = open('2231_input.txt')

def check(n):
    tot = 0
    while True:
        if n < 10:
            tot += n
            break
        tot += n%10
        n //= 10
    return tot

N = int(input())
for num in range(1, N+1):
    if num == N:
        ans = 0
    else:
        if num + check(num) == N:
        # if num + sum(list(map(int, str(num)))) == N:
            ans = num
            break
print(ans)