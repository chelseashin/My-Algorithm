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
    if num + check(num) == N:
    # 함수 만들지 않고 성공
    # if num + sum(list(map(int, str(num)))) == N:
        ans = num
        break
    else:
        ans = 0

print(ans)